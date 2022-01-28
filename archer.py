# -*- coding: utf-8 -*-

# Created by: Sri Ranga

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logindata
#import tes
import speech_recognition as sr
import pyaudio
import pyttsx3
import sys
import wolframalpha
from PyQt5 import  QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from archerui import Ui_MainWindow
import operator
from selenium.common.exceptions import NoSuchElementException
# initialisation
cl = wolframalpha.Client('LHV4RJ-7AGKTR2LVV')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.taskexec()

    def takecommand(self):
        global text
        # testing
        engine.say("Hello!What do you want me to do?")
        engine.runAndWait()
        # Initialize recognizer class (for recognizing the speech)
        r = sr.Recognizer()
        # Reading Microphone as source
        # listening the speech and store in audio_text variable
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Talk")
            print("Listening.............")
            try:
                r.pause_threshold = 1

                audio_text = r.listen(source , timeout = 600 )
                print("Time over, thanks")
            except Exception as e:
                print(e)

        try:
            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            # using google speech recognition

            text = r.recognize_google(audio_text)
            print("Text: " + text)

        except:
            engine.say("Sorry, I did not get that")

        return text


    def taskexec(self):

        self.text =self.takecommand()

        # opening the browser.....................
        if "Amazon" in self.text:

            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(executable_path=r"C:\Users\tumma\PycharmProjects\weedalpha\chromedriver.exe")

            action = ActionChains(driver)
            time.sleep(1)

            driver.get('http://www.amazon.in')
            try:
                firstLevelMenu = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, "#nav-link-accountList")))
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
            if "search" in self.text:
                # ..............this is  for searching...............
                str1 = self.text.split(" ")
                str1.remove("search")
                str1.remove("Amazon")
                if "for" in str1:
                    str1.remove('for')
                engine.say("searching Amazon for")
                engine.say(str1)
                engine.runAndWait()
                searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
                searchbar.send_keys(str1)
                searchbar.send_keys(Keys.ENTER)
                time.sleep(10)

            elif "track" in self.text:
                # ...........................................................
                engine.say("Searching your Latest order Tracking Details  in Amazon ")
                engine.runAndWait()
                reutrnorder = driver.find_element_by_xpath('//*[@id="nav-orders"]')
                reutrnorder.click()
                time.sleep(3)

                trackpackage = driver.find_element_by_xpath('//*[@id="a-autoid-3-announce"]')
                trackpackage.click()
                time.sleep(3)

                shippingdetails = driver.find_element_by_link_text('See all updates')
                shippingdetails.click()
                time.sleep(3)

                container = driver.find_element_by_id('tracking-events-container')
                time.sleep(3)

                trackingData = container.find_elements_by_css_selector('div.a-spacing-top-medium')
                time.sleep(3)
                trackingList = []

                for item in trackingData:
                    trackingList.append((item.text).split('\n'))

                time.sleep(3)

                # testing
                engine.say(trackingList)
                engine.runAndWait()
            else:
                # ..............this is  for searching...............
                str1 = self.text.split(" ")
                if "search" in str1:
                    str1.remove("search")
                str1.remove("Amazon")
                if "for" in str1:
                    str1.remove('for')
                engine.say("searching Amazon for")
                engine.say(str1)
                engine.runAndWait()
                searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
                searchbar.send_keys(str1)
                searchbar.send_keys(Keys.ENTER)
                time.sleep(10)


        elif "play" in self.text:

            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(executable_path=r"C:\Users\tumma\PycharmProjects\weedalpha\chromedriver.exe")
            action = ActionChains(driver)
            time.sleep(1)

            driver.get('https://www.youtube.com/')

            # ..............this is  for searching......................

            searchbar = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
            str1 = self.text.split(" ")
            str1.remove("play")
            time.sleep(6)
            searchbar.send_keys(str1)
            searchbar.send_keys(Keys.ENTER)
            time.sleep(13)

            firstvideo = driver.find_element_by_xpath( '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
            firstvideo.click()
            time.sleep(10)
            try:
                content = driver.find_element_by_xpath( '//*[@id="ad-text:7"]')
                content.click()
                time.sleep(3)
            except NoSuchElementException as exc:
                print("sorry cant skip Advertisement")


        elif "who" or "what" in self.text:
            scq = cl.query(self.text)
            try:

                sca = next(scq.results).text.encode('utf-8')
                print('The answer is: ' + str(sca))
                saa= sca.encode('utf-8')
                engine.say('The answer is: ' + "u"+str(saa))
                engine.runAndWait()
            except Exception as e:
                print(e)
                engine.say('Sorry Cannot give you an answer')
                engine.runAndWait()

        else:
            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truediv__,
                    'Mod': operator.mod,
                    'mod': operator.mod,
                    '^': operator.xor,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            engine.say(self.text + " is equal to")
            engine.say(eval_binary_expr(*(self.text.split())))
            engine.runAndWait()





startexec = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)
    def starttask(self):
        self.ui.movie=QtGui.QMovie("../../Downloads/tumblr_nrqm32yH3W1r6xm5co1_1280.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/is.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        startexec.start()

app=QApplication(sys.argv)
archer=Main()
archer.show()
exit(app.exec_())









