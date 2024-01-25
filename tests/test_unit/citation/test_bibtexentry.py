import pytest

from brainglobe.citation.bibtex_fmt import Article


class TestBibtexEntry:
    """
    Tests for the BibtexEntry class.

    We test on the Article class, since the BibtexEntry class is a
    factory for the individual bibtex-format classes so cannot be
    tested itself.
    """

    good_info = {
        "author": [{"given-names": "tester", "family-names": "testing"}],
        "title": "testing",
        "journal": "tested",
        "year": 2000,
    }
    opt_info = {
        "volume": "test",
        "number": 42,
        "pages": "42",
        "month": "test",
        "note": "test",
        "doi": "test",
        "issn": "test",
        "zblnumber": "test",
        "eprint": "test",
    }

    def test_bad_construction(self) -> None:
        """
        Test that:
        - Not providing a required key results in an error.
        - Providing an invalid author format raises an error.
        - Providing a bad citation key raises an error.
        """
        # Not providing a particular key
        pass_info = self.good_info.copy()
        pass_info.pop("author", None)
        with pytest.raises(
            KeyError, match="Did not receive value for required key: author"
        ):
            Article(information=pass_info)

        # Provide an invalid author format
        pass_info["author"] = "sensible name that's not in the expected format"
        with pytest.raises(
            TypeError,
            match="Expected author to be either dict or list of dicts, "
            "not str",
        ):
            Article(information=pass_info)

        # Provide an invalid citation key
        with pytest.raises(ValueError, match="Citation key .* is not valid."):
            Article(information=self.good_info, cite_key="a11g00dt111n0w:(")

    def test_nothrow_on_missing_optionals(self) -> None:
        """
        Test that optional fields can be skipped when specifying information.
        """
        Article(information=self.good_info)

    def test_warn_on_unused_info(self) -> None:
        """
        Test that, when requested, warnings are thrown if information is
        passed that will not be used in the citation.
        """
        pass_info = self.good_info | self.opt_info
        pass_info["random_info"] = 42

        with pytest.warns(
            UserWarning,
            match="The key random_info is not used"
            " for entries of type article",
        ):
            Article(information=pass_info, warn_on_not_used=True)

    def test_write(self) -> None:
        """
        Test that the expected output string is written when assembling a
        Bibtex entry.
        """
        raise NotImplementedError
