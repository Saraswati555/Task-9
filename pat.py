from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class LoginAutomation:
    """
    This class is used to login into the https://www.saucedemo.com/ webpage using the username and password

    url = https://www.saucedemo.com/
    username = standard_user
    password = secret_sauce
    """

    def __init__(self, url="https://www.saucedemo.com/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method is to open up the chrome browser with the URL and makes the browser to go fullscreen. Then waits for 3 seconds
        :return:
        """
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        """
        This method is used to close the web browser
        :return:
        """
        self.driver.quit()

    def login(self):
        self.boot()

        # This is to fill the username and the password
        self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
        sleep(3)
        self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
        sleep(3)
        # find the login button and click on it
        self.driver.find_element(by=By.ID, value="login-button").click()
        sleep(3)

        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("Login Successfully")
        else:
            print("Error")

    def get_title(self):
        return self.driver.title

    def CurrentURL(self):
        return self.driver.current_url

    def Entirecontent(self):
        return self.driver.page_source





# Example usage:
obj = LoginAutomation()
obj.login()
print(obj.get_title())
print(obj.CurrentURL())
print(obj.Entirecontent())
obj.quit()
