# In-memory set to store blacklisted numbers
blacklisted_numbers = frozenset()


def blacklist(number: int):
    """
    Add the specified value to the blacklist.
    """
    global blacklisted_numbers
    blacklisted_numbers = frozenset((number, *blacklisted_numbers))


def unblacklist(number: int):
    """
    Remove the specified value from the blacklist.
    """
    global blacklisted_numbers
    blacklisted_numbers = frozenset(x for x in blacklisted_numbers if not x == number)


def get_blacklisted():
    """
    Returns a generator which contains the blacklisted values.
    """
    yield from blacklisted_numbers
