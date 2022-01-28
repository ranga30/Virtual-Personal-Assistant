
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logindata
import tes
import speech_recognition as sr
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
engine.say("Hello!What do you want me to do?")
#engine.say("Thank you, Geeksforgeeks")
engine.runAndWait()
# Initialize recognizer class (for recognizing the speech)

#r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable


# opening the browser.....................


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome()
action = ActionChains(driver)
time.sleep(1)

driver.get('http://www.amazon.in')
try:
    firstLevelMenu =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav-link-accountList")))
    action = ActionChains(driver)
    action.move_to_element(firstLevelMenu).perform()
except Exception as e:
    print(e)

secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata.USERNAME)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(logindata.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)


#..............this is  for searching......................


searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbar.send_keys(tes.text)
searchbar.send_keys(Keys.ENTER)
time.sleep(3)

