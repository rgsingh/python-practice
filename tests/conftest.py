import pytest


# monkeypatch os.environ

@pytest.fixture(autouse=True)
def set_env_vars(monkeypatch):
    # Set the environment variable for the test
    monkeypatch.setenv("TEST_ENV_VAR", "test_value")
    monkeypatch.setenv("TEST_ENV_VAR2", "test_value2")
    monkeypatch.setenv("TEST_ENV_VAR3", "test_value3")
    monkeypatch.setenv("TEST_ENV_VAR4", "test_value4")
    monkeypatch.setenv("TEST_ENV_VAR5", "test_value5")
    monkeypatch.setenv("TEST_ENV_VAR6", "test_value6")
    monkeypatch.setenv("TEST_ENV_VAR7", "test_value7")
    monkeypatch.setenv("TEST_ENV_VAR8", "test_value8")

