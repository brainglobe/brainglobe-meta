from typing import Literal, Set

from brainglobe.citation.repositories import REPOSITORIES, Repository


def cite(
    *tools: str,
    format: Literal["bibtex"] = "bibtex",
    outfile: str = None,
    cite_software: bool = False,
) -> None:
    """
    Provide citation(s) for the BrainGlobe tool(s) that the user has supplied.

    If two or more aliases point to the same tool, remove duplicates and report
    the duplication has been ignored.

    Parameters
    ----------
    tools: str
        Tool names or aliases that are to be cited.
    format: One of bibtex, default = bibtex
        Reference format to write.
    outfile: str, default = None
        The output file to write to, if provided.
        If None, reference text will be printed to the console.
        File prefixes will be automatically appended if not present.
    cite_software: bool, default = False
        If True, software citations will be preferred over the article
        or journal counterparts, where present in repositories.
        Use if you want to reference the source code of a particular tool,
        rather than acknowledge use of the tool itself.
    """
    unique_repos: Set[Repository] = set()

    for tool in tools:
        repo_to_cite: Repository = None
        for repo in REPOSITORIES:
            if tool in repo:
                if repo:
                    # We have already found this alias in another repository,
                    # Flag error
                    raise ValueError(
                        f"Multiple repositories match tool {tool}: "
                        f"{repo_to_cite.name}, {repo.name}"
                    )
                else:
                    # This is the first repository that might match the tool
                    repo_to_cite = repo
        if repo_to_cite is None:
            # No repository matches this tool, throw error.
            raise ValueError(
                f"No citable repository found for tool {tool}. "
                "If you think this option is missing, please report it: "
                "https://github.com/brainglobe/brainglobe-meta/issues"
            )
        elif repo_to_cite in unique_repos:
            # We already added this repository, so print out a record
            # of the duplication
            print(f"{tool} is already being cited by {repo_to_cite.name}")
        else:
            # Add first occurrence of the repository to the unique list
            unique_repos.add(repo_to_cite)

    # unique_repos is now a set of all the repositories that we need to cite
    # so we just need to gather all the citations we need
    cite_string = ""

    for repo in unique_repos:
        # Fetch citation information from repository
        citation_info = repo.read_citation_info()
        if format == "sentence":
            # If the user requested the citation sentence,
            # provide this by looking up the expected field.
            raise NotImplementedError
        else:
            # We need to convert the citation information to
            # a particular format

            # First, check if there is a preferred-citation
            # field and use that information over the standard
            # software citation if requested.
            if citation_info["type"] == "software" and not cite_software:
                # We don't want to cite software if there is an academic
                # reference (journal, book, etc).
                # See if this is the case.
                if "preferred-citation" in citation_info.keys():
                    # Use the alternative citation, note that if it is a
                    # software citation then this will still be used.
                    citation_info = citation_info["preferred-citation"]

            # Cite this repository in the desired format
            if format == "bibtex":
                # INFER CITATION TYPE
                if True:
                    print(cite_string)
