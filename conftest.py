from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FireFoxOptions

import environment
import time
import pytest
import os
driver = None

def chrome_driver(mode):
    chrome_option = ChromeOptions()
    chrome_option.add_argument(mode)
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    chrome_option.add_argument("--ignore-certificate-errors")
    chrome_option.add_argument("--remote-allow-origins=*")
    return   webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)

def edge_driver(mode):
    edge_option = EdgeOptions()
    edge_option.add_argument(mode)
    edge_option.add_argument("--ignore-certificate-errors")
    return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_option)

def firefox(mode):
    firefox_option = FireFoxOptions()
    firefox_option.add_argument(mode)
    firefox_option.add_argument("--ignore-certificate-errors")
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_option)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=environment.BROWSER)
    parser.addoption("--env", action="store", default="qa")
    parser.addoption("--headmode", action="store", default="--head")


def feature_path():
    user_path = os.path.abspath("tests/features")
    return user_path

@pytest.fixture(scope='session')
def getBrowser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def getBrowserMode(request):
    return request.config.getoption("--headmode")

@pytest.fixture(scope='session')
def getUrl(request):
    if request.config.getoption("--env") == "qa":
        return environment.QA
    elif request.config.getoption("--env") == "stage":
        return environment.STAGE
    elif request.config.getoption("--env") == "prod":
        return environment.PROD
    else:
        return environment.QA


@pytest.fixture(scope='session', autouse=True)
def driver_init(getBrowser, getUrl, getBrowserMode):
    global driver
    
    if getBrowser == "chrome":
        driver = chrome_driver(getBrowserMode)
    elif getBrowser == "firefox":
        driver = firefox(getBrowserMode)
    elif getBrowser == "edge":
        driver = edge_driver(getBrowserMode)
    else:
        driver = chrome_driver(getBrowserMode)
    driver.get(getUrl)
    driver.maximize_window()
    # time.sleep(10)
    yield
    driver.quit()