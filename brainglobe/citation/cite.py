import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Literal
from warnings import warn

from brainglobe.citation.bibtex_fmt import (
    BibTexEntry,
    supported_bibtex_entry_types,
)
from brainglobe.citation.repositories import (
    all_citable_repositories,
    unique_repositories_from_tools,
)
from brainglobe.citation.text_fmt import TextCitation


def cite(
    *tools: str,
    format: Literal["bibtex", "text"] = "bibtex",
    outfile: Path = None,
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

        # Some formats are citation-type agnostic, others are not
        # Attempt to read this key here, and set the value to None
        # if it's not present.
        # This ensures that users don't have to provide the field if
        # they want to cite something that doesn't need the information.
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
            citation_type = citation_info["type"]

        # Determine citation format in preparation for writing
        if format == "text":
            # If the user requested the citation sentence,
            # provide this by looking up the expected field.
            reference_instance = TextCitation(
                citation_info, warn_on_not_used=True
            )
        else:
            # We need to convert the citation information to
            # a particular format

            # Cite this repository in the desired format
            if format == "bibtex":
                try:
                    citation_class = supported_bibtex_entry_types()[
                        citation_type
                    ]
                except KeyError:
                    raise ValueError(
                        f"Bibtex entries require a supported Bibtex entry type"
                        " to be provided in citation metadata "
                        f"(got {citation_type})"
                    )

                reference_instance: BibTexEntry = citation_class(
                    citation_info,
                    cite_key=f"{repo.name}",
                    warn_on_not_used=True,
                )

        # Append the reference to the string we are generating
        repo_reference = reference_instance.generate_ref_string()
        cite_string += f"{repo_reference}" + "\n" * newline_separations

    # Upon looping over each of the repositories, we should be ready to dump
    # the output to the requested location.
    if outfile is not None:
        # Fix file prefixes if necessary
        outfile = Path(outfile)
        extension = infer_prefix(format)
        if not outfile.suffix == extension:
            outfile = Path(f"{outfile.stem}.{extension}")

        # Write output to file
        with open(outfile, "w") as output_file:
            output_file.write(cite_string)
    else:
        sys.stdout.write(cite_string)

    return cite_string


def infer_format(requested_extension: Literal["tex", "txt"]) -> str:
    """
    Return the citation format to write given the prefix of the output
    file.

    This is the inverse of infer_prefix.
    """
    if requested_extension == "tex":
        return "bibtex"
    elif requested_extension == "txt":
        return "text"
    else:
        raise ValueError(
            "Cannot infer citation format from "
            f"extension {requested_extension}."
        )


def infer_prefix(output_format: Literal["bibtex", "text"]) -> str:
    """
    Return the file prefix to be used for the given output format.

    This is the inverse of infer_format.
    """
    if output_format == "bibtex":
        return "tex"
    elif output_format == "text":
        return "txt"
    else:
        raise ValueError(
            "I don't know what extension to "
            f"give outputs of format {output_format}"
        )


class BrainGlobeParser(ArgumentParser):
    """
    Overwrite argparse default behaviour to have usage errors
    print the command-line tool help, rather than throwing the
    error encountered.
    """

    def error(self, msg):
        sys.stderr.write(f"Error: {msg}\nSee usage instructions below:\n")
        self.print_help()
        sys.exit(2)


def cli() -> None:
    """
    Command-line interface for the citation tool.
    """
    parser = BrainGlobeParser(
        description="Citation generation for BrainGlobe tools."
    )

    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List citable BrainGlobe tools, and formats, then exit.",
    )
    parser.add_argument(
        "-s, --software-citations",
        action="store_true",
        help="Explicitly cite software source code over academic papers.",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        nargs=1,
        type=str,
        default=None,
        help="Output file to write citations to.",
    )
    parser.add_argument(
        "-f",
        "--format",
        nargs=1,
        type=str,
        help="Citation format to write. "
        "Will overwrite the inferred format if the output file "
        "argument is also provided. "
        "Valid formats can be listed with the -l, --list option.",
    )
    parser.add_argument("tools", nargs="+")

    arguments = parser.parse_args()

    # Check if we just want to list available options
    if arguments.list:
        # List citable BrainGlobe tools
        sys.stdout.write("Citable BrainGlobe tools by name (source code):\n")
        for repo in sorted(all_citable_repositories()):
            sys.stdout.write(f"\t- {repo.name} ({repo.url})\n")

        # List reference formats
        sys.stdout.write(
            "Available citation formats (format, file extension):\n"
        )
        sys.stdout.write("\t- BibTex (*.tex)\n")
        sys.stdout.write("\t- Text (*.txt)\n")

        # Terminate
        sys.exit(0)

    # Pass default values if available
    fmt = "bibtex"
    output_file = None

    # Check for custom options from CLI
    if hasattr(arguments, "format"):
        fmt = arguments.format
        try:
            infer_prefix(fmt)
        except ValueError as e:
            # This output format is not supported!
            raise RuntimeError(f"Output format {fmt} is not supported.") from e

    if hasattr(arguments, "output_file"):
        output_file = Path(arguments.output_file)
        extension = output_file.suffix

        # Output file was provided, attempt to infer format from this
        # if not provided explicitly
        if fmt is None:
            try:
                fmt = infer_format(extension)
            except ValueError as e:
                # Output file has an unknown extension, but the user has
                # not requested a particular format.
                raise RuntimeError(
                    f"Citation file format {extension} is not supported."
                ) from e

    # Invoke API function
    cite(
        *arguments.tools,
        format=fmt,
        outfile=output_file,
        cite_software=arguments.software_citations,
    )
    sys.exit(0)
