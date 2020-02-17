"""
Some rather arbitrary and contrived test examples.
"""
from unittest import mock
from piglatin import translate


def test_translate():
    """
    PyTest uses simple assert statements to validate outcomes in tests.
    """
    sentence = "Hello there. How are you?"
    result = translate(sentence)
    expected = "Ellohay heretay. Owhay areay ouyay?"
    assert expected == result


def test_translate_splits_string():
    """
    We can use a mock to spy on how our code behaves.
    """
    sentence = mock.MagicMock()
    sentence.split.return_value = ["Hello", "there",]
    translate(sentence)
    assert sentence.split.call_count == 1
