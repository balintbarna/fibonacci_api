# In-memory set to store blacklisted numbers
blacklisted_numbers = set()


def blacklist(number: int):
    """
    Add the specified value to the blacklist.
    """
    blacklisted_numbers.add(number)


def unblacklist(number: int):
    """
    Remove the specified value from the blacklist.
    """
    blacklisted_numbers.remove(number)


def get_blacklisted():
    """
    Returns a generator which contains the blacklisted values.
    """
    yield from blacklisted_numbers
