from brainglobe.citation.cite import cite


def test_citation_combinations(newline_separations: int = 2) -> None:
    """
    Test that when citing multiple tools, the resulting text is the
    combination of requesting the two tools individually.
    """

    both_together = cite(
        "brainglobe-meta",
        "bg-atlasapi",
        newline_separations=newline_separations,
    )
    bg_meta = cite("brainglobe-meta")
    bg_atlasapi = cite("bg-atlasapi")

    # Fetching both citations together should mean the text from the
    # individual citations is included
    assert bg_meta in both_together and bg_atlasapi in both_together, (
        "Fetching multiple tools at once"
        "does not generate all requested citations."
    )
    # Removing these individual blocks of text from the combined citation
    # should leave only newline and whitespace characters
    leftover_text = (
        both_together.replace(bg_meta, "")
        .replace(bg_atlasapi, "")
        .replace(" ", "")
        .replace("\n", "")
    )
    assert (
        not leftover_text
    ), f"Leftover text in combined citation: {leftover_text}"
