from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from utilities.customLogger import LogGen

def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="Chrome"
    )


@pytest.fixture()
def setup(request):
    logger=LogGen.loggen()
    Browser_name=request.config.getoption("--browserName")
    if Browser_name == 'Chrome':
        logger.info("=========chrome browser Intialize=============")
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        return driver

    elif Browser_name=="Firefox":
        logger.info("=========Firefox browser Intialize=============")
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif Browser_name=="IE":
        logger.info("=========Ie browser Intialize=============")
        driver = webdriver.Ie(IEDriverManager().install())

    elif Browser_name=="Safari":
        logger.info("=========Safari browser Intialize=============")
        driver = webdriver.Safari()
    return driver
        
###############customize hooks for html reports################
#Adding Enviorment info####
def pytest_configure(config):
    config._metadata['Project Name']='ecoomerce website'
    config._metadata['Module Name']='listing'
    config._metadata['Tester Name']='Saurabh Patyal'

#This hook wil modify Enviornment info to Html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)