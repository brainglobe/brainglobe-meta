import warnings
from string import ascii_letters, digits
from typing import Any, ClassVar, Dict, List


class BibTexEntry:
    """
    An abstract base class for generating BibTex entries from
    CITATION.cff yaml-content.

    Constructed by passing a dict containing the yaml-processed
    content of the CITATION.cff file to the constructor.
    Required fields are checked for on instantiation.
    Missing optional fields will be set to None if not provided.

    Parameters
    ----------
    information : Dict[str, str]
        yaml-processed content of CITATION.cff.
    cite_key : str, default = "BrainGlobeReference"
        Citation key to add to the BibTex reference that is generated.
    warn_on_not_used: bool, default = False
        If True, warn the user about the fields in the information
        input that are not required nor optional, so are ignored.

    Attributes
    ----------
    cite_key : str
        The citation key that appears in the BibTex reference
    entry_type : ClassVar[str]
        The BibTex entry type; article, book, software, etc
    required : ClassVar[List[str]]
        Required fields for the entry to be created
    optional : ClassVar[List[str]]
        Optional fields that the entry may possess
    indent_character : str, default = ' ' * 4
        Character sequence to use for indentation.
    """

    # The citation key that appears in the BibTex reference
    cite_key: str
    # The BibTex entry type; article, book, software, etc
    entry_type: ClassVar[str]
    # Required fields for the entry to be created
    required: ClassVar[List[str]]
    # Optional fields that the entry may possess
    optional: ClassVar[List[str]]

    # Character sequence to use for indentation
    indent_character: str = " " * 4

    # mypy type-hints
    author: str | Dict[str, str] | List[Dict[str, str]]

    @classmethod
    def validate_citation_key(cls, key: str) -> bool:
        """
        Return True if the citation key provided is valid for use,
        otherwise return False.

        Valid citation keys may contain;
        - Alphanumeric characters,
        - Underscores (_),
        - Single dashes (-),
        - Semicolons (:),

        and no others.
        """
        bad_characters = key.lower()
        for char in ascii_letters + digits + "_-:":
            bad_characters = bad_characters.replace(char, "")

        if bad_characters:
            # Some characters in the string provided are not permitted,
            # as we have removed all of the permitted characters.
            return False
        return True

    def __init__(
        self,
        information: Dict[str, Any],
        cite_key: str = "BrainGlobeReference",
        warn_on_not_used: bool = False,
    ) -> None:
        """ """
        # Add the citation key if provided,
        # or use the default otherwise
        if self.validate_citation_key(cite_key):
            self.cite_key = cite_key
        else:
            raise ValueError(
                f"Citation key {cite_key} is not valid."
                " Citation keys may only be composed of"
                "alphanumeric characters, digits, '_', '-', and ':'"
            )

        # Add all the information we need
        for key, value in information.items():
            if key in self.required or key in self.optional:
                setattr(self, key, value)
            elif warn_on_not_used:
                warnings.warn(
                    f"The key {key} is not used for entries of type "
                    f"{self.entry_type}",
                    UserWarning,
                )

        # Check that all required information is populated
        for required_field in self.required:
            if not hasattr(self, required_field):
                raise KeyError(
                    f"Did not receive value for required key: {required_field}"
                )
        # Optional fields should be set to None so that checks against
        # them produce nothing and evaluated to False
        for optional_field in self.optional:
            if not hasattr(self, optional_field):
                setattr(self, optional_field, None)

        # If we have an author field, we will need to parse the
        # dictionary input into the string that BibTex is expecting
        if hasattr(self, "author"):
            self._prepare_author_field()

        return

    def _prepare_author_field(self) -> None:
        """
        The authors field may come in as a dict, or a list of dicts.
        This is rather inconvenient as we need it to be a string, so
        convert it with this function.

        author fields in CITATION.cff are:
        - family-names
        - given-names
        - orcid
        - affiliation

        or which we only need the names.
        """
        # A single author will be read in as a dictionary
        if isinstance(self.author, dict):
            surname = self.author["family-names"]
            forename = self.author["given-names"]
            self.author = f"{forename} {surname}"
        # Multiple authors will be read in as a list of dictionaries
        elif isinstance(self.author, list):
            all_authors = []
            for author_info in self.author:
                if not isinstance(author_info, dict):
                    raise ValueError(
                        f"Expected author to be dictionary but it was"
                        f" {type(author_info)}: {author_info}"
                    )
                else:
                    surname = author_info["family-names"]
                    forename = author_info["given-names"]
                    all_authors.append(f"{forename} {surname}")
            self.author = "and".join(all_authors)
        # Unrecognised read format, abort
        else:
            raise TypeError(
                f"Expected author to be either dict or list of dicts,"
                f" not {type(self.author).__name__}"
            )
        return

    def write(self) -> str:
        """
        Write the appropriate reference text,
        using the populated fields.
        """
        output_string = f"@{self.entry_type}{{{self.cite_key},"

        # Tracks current indentation level
        indent_level = 1

        # Required fields are guaranteed to exist
        for req_field in self.required:
            output_string += (
                self.indent_character * indent_level
                + f'{req_field} = "{getattr(self, req_field)}",\n'
            )

        # Optional fields may be skipped
        for opt_field in self.optional:
            if getattr(self, opt_field):
                output_string += (
                    self.indent_character * indent_level
                    + f'{opt_field} = "{getattr(self, opt_field)}",\n'
                )

        indent_level -= 1
        output_string += "}"

        return output_string


class Article(BibTexEntry):
    """
    Derived BibtexEntry for creating article entries.
    """

    entry_type = "article"
    required = ["author", "title", "journal", "year"]
    optional = [
        "volume",
        "number",
        "pages",
        "month",
        "note",
        "doi",
        "issn",
        "zblnumber",
        "eprint",
    ]
    # def __init__(self, *args, **kwargs):
    #     self.entry_type = "article"
    #     self.required = ["author", "title", "journal", "year"]
    #     self.optional = [
    #         "volume",
    #         "number",
    #         "pages",
    #         "month",
    #         "note",
    #         "doi",
    #         "issn",
    #         "zblnumber",
    #         "eprint",
    #     ]
    #     super().__init__(*args, **kwargs)
