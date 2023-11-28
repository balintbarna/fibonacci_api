from requests import get, post, delete


BASE_URL = 'http://localhost:8080'
FIRST_TEN_VALUES = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)


def request_result(index: int):
    return get(f'{BASE_URL}/api/fibonacci/{index}')


def blacklist(value: int):
    return post(f'{BASE_URL}/api/blacklist/{value}')


def unblacklist(value: int):
    return delete(f'{BASE_URL}/api/blacklist/{value}')


def single_value_routine():
    assert request_result(6).json()['value'] == 8
    assert request_result(-1).status_code == 500
    assert blacklist(8).status_code == 200
    bad_request = request_result(6)
    assert bad_request.status_code == 500
    assert 'ValueError: The result is blacklisted.' in bad_request.text
    assert unblacklist(8).status_code == 200
    assert request_result(6).json()['value'] == 8


def list_routine():
    values = get(f'{BASE_URL}/api/fibonaccis/0').json()['value']
    assert type(values) == list
    values = tuple(values)
    assert len(values) == 100
    assert values[:10] == FIRST_TEN_VALUES
    assert len(get(f'{BASE_URL}/api/fibonaccis/0', params=[('size', '10')]).json()['value']) == 10
    assert get(
        f'{BASE_URL}/api/fibonaccis/1').json()['value'][0] == 354224848179261915075
    assert blacklist(8).status_code == 200
    less_values = tuple(get(f'{BASE_URL}/api/fibonaccis/0').json()['value'])
    assert len(less_values) == 99
    assert less_values[:9] == tuple(x for x in FIRST_TEN_VALUES if not x == 8)
    assert 8 not in less_values
    assert unblacklist(8).status_code == 200


if __name__ == '__main__':
    single_value_routine()
    list_routine()
