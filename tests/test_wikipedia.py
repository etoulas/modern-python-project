from modern_python_project import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="el")
    args, _ = mock_requests_get.call_args
    assert "el.wikipedia.org" in args[0]