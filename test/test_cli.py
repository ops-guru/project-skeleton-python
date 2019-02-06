import pytest

from company_tool import cli


def test_parse_argv():
    expected = dict(
        iparam=str(123),
        sparam='jaasdsdas_asdas',
        workdir='/tmp',
    )
    args = [
        expected.get('iparam'),
        expected.get('sparam'),
        '--workdir', expected.get('workdir'),
    ]
    actual = cli.parse_args(args=args)
    assert int(expected.get('iparam')) == actual.iparam
    assert expected.get('sparam') == actual.sparam
    assert expected.get('workdir') == actual.workdir
