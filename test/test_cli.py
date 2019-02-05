import pytest

from company.tool import cli


def test_parse_argv():
    expected_runid = '123'
    expected_numflows = '321'
    expected_workdir = '/tmp'
    expected_bucket = 'kuku'
    expected_remote = '/lala/kuka'
    argv = [
        '123',
        '321',
        '--workdir', expected_workdir ,
        '--bucket', expected_bucket,
        '--remote', expected_remote
    ]
    actual = cli.parse_args(argv)
    assert int(expected_runid) == actual.RunID
    assert int(expected_numflows) == actual.Flows
    assert expected_workdir == actual.workdir
    assert expected_bucket == actual.bucket
    assert expected_remote == actual.remote