from backend.parser import extract_text


def test_extract_text_exists():

    assert callable(
        extract_text
    )