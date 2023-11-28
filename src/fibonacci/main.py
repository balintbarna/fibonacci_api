from bottle import Bottle, request, response, run
#
from .fibonacci_math import get_fibonacci_value


app = Bottle()


@app.route('/api/fibonacci/<index>', method='GET')
def get_result(index: str):
    return {'value': get_fibonacci_value(int(index))}


@app.route('/api/fibonaccis/<page>', method='GET')
def get_list(page: str):
    size = int(request.query.get('size', 100))
    start_index = int(page) * size
    stop_index = start_index + size
    return {'value': [get_fibonacci_value(x) for x in range(start_index, stop_index)]}


def main():
    run(app, host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    main()
