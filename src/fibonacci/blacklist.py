# In-memory set to store blacklisted numbers
blacklisted_numbers = set()


def blacklist(number: int):
    blacklisted_numbers.add(number)


def unblacklist(number: int):
    blacklisted_numbers.remove(number)


def get_blacklisted():
    yield from blacklisted_numbers
