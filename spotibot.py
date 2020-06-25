from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class SpotifyC():#Chrome
    PROXY = "163.172.227.13:5836"
    #path_d = "C:\\Users\\User\\Desktop\\chromedriver_win32\\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    driver = None
    # <element id>
    IdUsername = "login-username"
    IdPassword = "login-password"
    IdLogBut = "login-button"
    #</element id>
    def __init__(self,driver_path = "C:\\Users\\User\\Desktop\\chromedriver_win32\\chromedriver.exe", proxy = [False,""]):
        if proxy[0]:
            if(proxy[1]):
                self.PROXY = proxy[1]
            self.chrome_options.add_argument('--proxy-server=%s' % self.PROXY)
        self.driver = webdriver.Chrome(driver_path,chrome_options=self.chrome_options)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(15)
    def LogIn(self,login_sp,password_sp):
        element = self.driver.find_element_by_class_name("_1edf52628d509e6baded2387f6267588-scss")
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.implicitly_wait(15)
        login = self.driver.find_element_by_id(self.IdUsername).send_keys(login_sp)
        password = self.driver.find_element_by_id(self.IdPassword).send_keys(password_sp)
        login_button = self.driver.find_element_by_id(self.IdLogBut)
        self.driver.execute_script("arguments[0].click();", login_button)
        self.driver.implicitly_wait(15)
        print("\n\tLogIn Complete!")
    def GetPageDriver(self, url):
        self.driver.get(url)
        
if __name__ == "__main__":
    chrome = SpotifyC(driver_path = path_d, proxy = [True,"185.174.101.253:4045"], )
    chrome.driver.get("https://open.spotify.com/album/1fQL5ZynvGJmJAybF0SwvT?si=m80eYaZoSve67eTFHdaQOA")
    chrome.LogIn(login_sp = "arnold2020@gmail.com", password_sp = "Qwerty112233")
    chrome.driver.implicitly_wait(15)
    elem = chrome.driver.find_element_by_class_name("_11f5fc88e3dec7bfec55f7f49d581d78-scss")
    forward = chrome.driver.find_element_by_xpath("//button[@data-testid='control-button-skip-forward']")
    chrome.driver.execute_script("arguments[0].click();", elem)
    val=0
    while val!=10:
        slp = random.randint(40,60)
        print(slp,"\n")
        time.sleep(slp)
        chrome.driver.execute_script("arguments[0].click();", forward)
        val+=1
    chrome.driver.close()
    
