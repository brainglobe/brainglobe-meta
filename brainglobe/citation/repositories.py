from dataclasses import dataclass
from typing import Any, Dict, List

import requests

from brainglobe.citation.fetch import fetch_from_github, yaml_str_to_dict


@dataclass
class Repository:
    """
    Static class for representing GitHub repositories, in particular
    when needing to fetch CITATION information from them.

    Parameters
    ----------
    See attributes.

    Attributes
    ----------
    name : str
        The name of the repository.
    tool_aliases: List[str]
        Names by which the tool the repository provides might be called.
    cff_branch: str, default = "main"
        Branch on which the citation file can be found.
    cff_loc: str, default = "CITATION.cff"
        Location of the citation file on the appropriate branch.
    org: str, default = "brainglobe"
        Organisation or user to which the repository belongs.
    """

    name: str
    tool_aliases: List[str]
    cff_branch: str = "main"
    cff_loc: str = "CITATION.cff"
    org: str = "brainglobe"

    @property
    def url(self) -> str:
        """
        URL to the repository as hosted on GitHub.
        """
        return f"https://github.com/{self.org}/{self.name}"

    def __contains__(self, alias: str) -> bool:
        """
        Syntactic sugar to allow the use of
        if alias in Repository,
        when asking if a Repository is known by the given alias.

        Comparison is case-insensitive for added protection.
        """
        return alias.lower() in [name.lower() for name in self.tool_aliases]

    def __post_init__(self) -> None:
        """
        Validate the repository actually exists and is reachable,
        before attempting to fetch content later.

        Also ensure that a tool can be referred to by its repository
        name.
        """
        ping_site = requests.get(self.url)
        if not ping_site.ok:
            if ping_site.status_code == 404:
                # Site not found, so repository does not exist
                raise ValueError(
                    f"Repository {self.org}/{self.name} does not exist"
                    " (got 404 response)"
                )
            else:
                raise ValueError(
                    f"Could not reach {self.url} successfully (non 404 status)"
                )

        # Can always refer to yourself by repository name
        if self.name not in self.tool_aliases:
            self.tool_aliases.append(self.name)
        return

    def read_citation_info(self) -> Dict[str, Any]:
        """
        Read citation information from the repository into a dictionary.
        """
        cff_response = fetch_from_github(
            self.org, self.name, self.cff_loc, self.cff_branch
        )

        return yaml_str_to_dict(cff_response.text)


# Using the above class, we now define the repositories
# that contain tools that we might want users to be able to
# cite easily.
bg_atlasapi = Repository(
    "bg-atlasapi",
    ["BrainGlobe AtlasAPI", "BrainGlobe AtlasAPI", "AtlasAPI", "Atlas API"],
    cff_branch="add-citation-file",
)

REPOSITORIES = [bg_atlasapi]
