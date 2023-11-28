# Fibonacci API

Description placeholder...

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
