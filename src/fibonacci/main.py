from bottle import Bottle, request, response, run
#
from .fibonacci_math import get_fibonacci_value
from .blacklist import blacklist, unblacklist, get_blacklisted


app = Bottle()


@app.route('/api/fibonacci/<index>', method='GET')
def get_result(index: str):
    return {'value': get_fibonacci_value(int(index))}


@app.route('/api/fibonaccis/<page>', method='GET')
def get_list(page: str):
    size = int(request.query.get('size', 100))
    start_index = int(page) * size
    stop_index = start_index + size
    results = [get_fibonacci_value(x) for x in range(start_index, stop_index)]
    return {'value': [x for x in results if x not in get_blacklisted()]}


@app.route('/api/blacklist/<number>', method='POST')
def blacklist_number(number):
    blacklist(int(number))
    return {'status': 'success', 'message': f'Number {number} has been blacklisted.'}


@app.route('/api/blacklist/<number>', method='DELETE')
def unblacklist_number(number):
    unblacklist(int(number))
    return {'status': 'success', 'message': f'Number {number} has been removed from the blacklist.'}


def main():
    run(app, host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    main()
