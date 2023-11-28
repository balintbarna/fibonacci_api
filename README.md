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

The test using HTTP requests can be run by opening a new terminal session while the server is running,
activating the virtual environment, and running `python integration_testing/try_with_requests.py`.

The reason for creating the separate requests client based testing routine besides the pytest unittests
is to show how the last layer of the server can be tested from outside of the main python program.

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
