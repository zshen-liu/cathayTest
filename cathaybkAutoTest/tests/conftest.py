import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .config import ConfigManager

@pytest.fixture(scope='session', autouse=True)
def browser():
    chrome_options = Options()
    # adjust the chrome size for mobile view
    chrome_options.add_argument("--window-size=600,1200")
    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.close()
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--env", type=str, action="store", default="cathayRel",
        help="env, default: 'cathayRel'"
    )

@pytest.fixture(scope='session')
def set_config_from_cmd(pytestconfig):
    env = pytestconfig.getoption("env")
    env_config = ConfigManager(env).get_current_config()
    return env_config