from pytest import raises
from fibonacci import blacklist, unblacklist, get_blacklisted


def test_empty_blacklist():
    assert len(list(get_blacklisted())) == 0


def test_bad_remove():
    assert 1 not in get_blacklisted()
    with raises(KeyError):
        unblacklist(1)


def test_blacklisting_multiple_numbers():
    values = [3, 5, 9, 12, 34]
    for v in values:
        assert v not in get_blacklisted()
    for v in values:
        blacklist(v)
    for v in values:
        assert v in get_blacklisted()
    for v in values:
        unblacklist(v)
    for v in values:
        assert v not in get_blacklisted()


def test_concurrency_issue_with_reading_blacklist():
    for v in range(5):
        blacklist(v)
    for v in get_blacklisted():
        unblacklist(v)
