from typing import Dict, List

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

    @pytest.mark.parametrize(
        "author_info, expected",
        [
            pytest.param(
                {"given-names": "T.", "family-names": "Ester"},
                "T. Ester",
                id="Standalone dict",
            ),
            pytest.param(
                [
                    {"given-names": "T.", "family-names": "Ester"},
                    {"given-names": "A Sr.", "family-names": "Developer"},
                ],
                "T. Ester and A Sr. Developer",
                id="List of dicts",
            ),
        ],
    )
    def test_author_parsing(
        self, author_info: Dict[str, str] | List[Dict[str, str]], expected: str
    ) -> None:
        """
        Test that author information is parsed correctly when given as either
        a single dict, or a list of dicts.

        author_info is the information to be passed and processed by
        _prepare_author_field.
        expected is the string that we expect to be produced after this method
        returns.
        """
        pass_info = self.good_info.copy()
        pass_info["author"] = author_info

        article = Article(pass_info, warn_on_not_used=True)

        assert article.author == expected

    def test_generate_ref_string(self) -> None:
        """
        Test that the expected output string is written when assembling a
        Bibtex entry.

        We test on the Article class, but are really only calling methods
        from the base BibtexEntry class.
        """
        pass_info = self.good_info | self.opt_info
        citation_key = "TESTING123"

        article = Article(
            pass_info, cite_key=citation_key, warn_on_not_used=False
        )

        generated_text = article.generate_ref_string()
        lines_of_text = generated_text.split("\n")

        # Length of lines_of_text should be at least
        # 2 (cite-key header and closing bracer) + number of required fields
        # lines long
        assert len(lines_of_text) >= 2 + len(article.required)

        # First line should be @<type>{<cite_key>,
        assert lines_of_text[0] == f"@article{{{citation_key},"
        # Final line should be the closing bracer only
        assert lines_of_text[-1] == "}"

        # Intermediary lines are a bit trickier,
        # but they should all be of the form
        # <indent><field> = "<value>"
        # with the "author" field having a slightly different value
        intermediary_lines = lines_of_text[1:-1]
        potential_fields = article.required + article.optional

        for key, value in pass_info.items():
            if key != "author":
                expected_line = f'{article.indent_character}{key} = "{value}",'
            else:
                # Hard-code expected author pre-processing,
                # tested above in test_author_parsing
                expected_line = (
                    f'{article.indent_character}author = "tester testing",'
                )

            # Check that this is at least one of the lines,
            # if there is the possibility that the information should be
            # included in the reference.
            if key in potential_fields:
                # Annoying PEP8 mypy formatting things
                error_line = (
                    f"Value corresponding to {key} "
                    "missing from generated string."
                )
                assert expected_line in intermediary_lines, error_line
            # Otherwise, assert that information that was not needed
            # has been ignored
            else:
                error_line = (
                    f"Information for {key} was included in generated string"
                    " when it should have been ignored."
                )
                assert expected_line not in intermediary_lines, error_line
