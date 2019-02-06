import pytest

from company_tool.shared import thing


def test_shared_function():

    s = 'a'
    sep = ':'
    expected = 'got{sep}{s}'.format(**locals())
    actual = thing.shared_function(s)
    assert expected == actual

    sep = '-'
    expected = 'got{sep}{s}'.format(**locals())
    actual = thing.shared_function(s, sep=sep)
    assert expected == actual
