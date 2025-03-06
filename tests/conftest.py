import pytest, sys, random, py, pytest, os
from xprocess import ProcessStarter
from app import app


@pytest.fixture
def web_client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_web_address(xprocess):
    # Define the Python executable and Flask app path
    python_executable = sys.executable
    app_file = py.path.local(__file__).dirpath("../app.py")

    # Randomly pick an available port
    port = str(random.randint(5000, 5999))

    # Define the Starter class to start the Flask app
    class Starter(ProcessStarter):
        env = {"PORT": port, "APP_ENV": "test", **os.environ}
        pattern = (
            "Debugger PIN"  # Wait for this pattern to indicate the server is ready
        )
        args = [python_executable, app_file]

    # Ensure Flask app is running in the background
    xprocess.ensure("flask_test_server", Starter)

    # Return the address where the Flask app is running
    yield f"localhost:{port}"

    # Terminate the Flask app after the test is complete
    xprocess.getinfo("flask_test_server").terminate()
