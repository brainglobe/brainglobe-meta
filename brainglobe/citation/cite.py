from typing import Literal
from warnings import warn

from brainglobe.citation.bibtex_fmt import supported_entry_types
from brainglobe.citation.repositories import (
    unique_repositories_from_tools,
)


def cite(
    *tools: str,
    format: Literal["bibtex", "text"] = "bibtex",
    outfile: str = None,
    cite_software: bool = False,
    newline_separations: int = 2,
) -> str:
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
    newline_separations: int, default = 2
        Number of newline characters to use when separating references, in the
        event that multiple tools are to be cited.

    Returns
    -------
    str
        The string of citation text that was produced, in the requested format.

    Raises
    ------
    ValueError
        If the citation data fetched is missing a type specifier, and the
        format requested requires this to be explicitly set.
    """
    unique_repos = unique_repositories_from_tools(
        *tools, report_duplicates=True
    )

    # unique_repos is now a set of all the repositories that we need to cite
    # so we just need to gather all the citations we need
    cite_string = ""

    for repo in unique_repos:
        # Fetch citation information from repository
        citation_info = repo.read_citation_info()
        try:
            citation_type = citation_info["type"]
        except KeyError as e:
            warn(
                f"{repo.name} has no citation type data - "
                "reference may not be generated correctly.\n"
                f"(Caught {str(e)})",
                UserWarning,
            )
            citation_type = None

        # The repo_reference variable will contain the reference string
        repo_reference: str = None

        # Determine citation format in preparation for writing
        if format == "text":
            # If the user requested the citation sentence,
            # provide this by looking up the expected field.
            raise NotImplementedError
        else:
            # We need to convert the citation information to
            # a particular format

            # Check if there is a preferred-citation field,
            # and whether we want to use that information over the standard
            # software citation.
            # Note that if the alternative citation is also a software
            # citation, it will still be rendered as such.
            if (
                citation_type == "software"
                and not cite_software
                and "preferred-citation" in citation_info.keys()
            ):
                citation_info = citation_info["preferred-citation"]

            # Cite this repository in the desired format
            if format == "bibtex":
                try:
                    citation_class = supported_entry_types()[citation_type]
                except KeyError:
                    raise ValueError(
                        f"Bibtex entries require a supported Bibtex entry type"
                        " to be provided in citation metadata "
                        f"(got {citation_type})"
                    )

                repo_reference = citation_class(citation_info)

        # Append the reference to the string we are generating
        cite_string += f"{repo_reference}" + "\n" * newline_separations

    # Upon looping over each of the repositories, we should be ready to dump
    # the output to the requested location.
    if outfile is not None:
        with open(outfile, "w") as output_file:
            output_file.write(cite_string)
    else:
        print(cite_string)

    return cite_string
