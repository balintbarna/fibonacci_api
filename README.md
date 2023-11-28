# Fibonacci API

This projects implements a simple backend server based on Python and bottle
to calculate fibonacci results with some additional features detailed below.

## Run

1. Start with having a modern version of Python installed, such as 3.11 or newer.
1. Then clone the project using git
1. Open a terminal and navigate to the project root directory.
1. Finally, run the commands below:

```
python -m venv venv  # only on first run to create venv
./venv/Scripts/activate  # from the second run on to activate venv
pip install -e .
pytest  # check that results are all green
fibonacci_server  # starts the server, quits with Ctrl+C
```

The test using HTTP requests can be run by opening a new terminal session in the same directory
while the server is running, activating the virtual environment,
and running `python integration_testing/try_with_requests.py`.

## Considerations

The reason for creating the separate requests client based testing routine besides the pytest unittests
is to show how the last layer of the server can be tested from outside of the main python program.
Alternatively, this could also be handled as a pytest routine by created a multithreaded fixture
which runs the server while the test routines are called.

The server used in this project is bottle, which uses synchronous python APIs to handle connections.
This can cause the server to slow down when it receives many requests in quick succession.
To fix this issue, a library exists which monkey-patches networking python functions to work
asynchronously.
Alternatively, a different framework could be used.

Parallel calls to the functions that update the blacklist could interfere with each other, namely
when two successive calls want to modify the blacklist, one of them could erronously overwrite the
action of the other. This can be mitigated with a synchronising mechanism around the list overwrite.

There is a caching mechanism on the fibonacci calculation, which could take up a lot of memory over time.
It is also possible that at some size using the cache becomes slower than doing the calculation.
One should profile the performance implications of the cache and either remove it or set a maximum
size that yields the best result.

The fibonacci calculation is implemented via a recursive function. This is a very simple and elegant
solution, however it also means that the request quickly reaches the maximum recursion limit.
One could increase the the maximum limit, however that can be quite detrimental to performance in Python.
Instead an iterative implementation could be achieved with a queue which always contains the last 2
values during the calculation. The resulting code will be harder to read and perhaps slower, but
free from the recursion limit.

The error handling is a little bit barebones. The bottle framework handles Python exceptions gracefully,
returning a helpful error page with an error message referencing the exception. This is great for
the original developers but less useful for someone external trying to use the API.
As a future improvement, it could be beneficial to strictly check for invalid types and values and
provide a simpler custom error value in the response.

## APIs

- TYPE: GET
- URL: `/api/fibonacci/<index>`
- PARAMETERS
  - index: the index of the fibonacci number, positive integer
- RETURNS: A JSON dictionary such as {'value': result}, result is an integer number. Blacklisted return values result in an error (500).

---

- TYPE: GET
- URL: `/api/fibonaccis/<page>?size=N`
- PARAMETERS
  - page: the page index specifies which chunk of the results is returned, positive integer
  - size: specifies how many numbers should be considered in the result list, positive integer
- RETURNS: A JSON dictionary such as {'value': [results]}, where results is a maximum 'size' length list that contains fibonacci values in a paginated way. The list contains the requested page without the blacklisted values.

---

- TYPE: POST
- URL: `/api/blacklist/<number>`
- PARAMETERS
  - number: the value that should be added to the blacklist
- RETURNS: A friendly success message formatted as a JSON dictionary.

---

- TYPE: DELETE
- URL: `/api/blacklist/<number>`
- PARAMETERS
  - number: the value that should be removed from the blacklist
- RETURNS: A friendly success message formatted as a JSON dictionary.
