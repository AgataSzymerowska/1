from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Driver:
    def __init__(self):
        self.caps = DesiredCapabilities().CHROME
        self.caps["pageLoadStrategy"] = "eager"
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=self.caps)
        self.driver.maximize_window()
        self.driver.get("https://bluemedia.pl/kontakt")
