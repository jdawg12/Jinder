from selenium import webdriver
from time import sleep
from boonk import username, password
import subprocess, json, sys, random, time, os, re
from datetime import datetime, timedelta


class JinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(5)

        login_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button') #inspect the Facebook Login button and copy as Xpath. (not full xpath)
        login_btn.click()

        #Switching to popup window
        base_window = self.driver.window_handles[0]
        popup_window = self.driver.window_handles[1]
        self.driver.switch_to.window(popup_window)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pwd_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pwd_in.send_keys(password)

        fblogin_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fblogin_btn.click()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])

        allow_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_btn.click()

        notif_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        notif_btn.click()

        self.driver.switch_to.window(self.driver.window_handles[0])

    def like(self):
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]')
        # like_btn.click()
        # likebtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]')
        # likebtn.click()

        likebtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        likebtn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def swiperyesswiping(self):
        for x in range(6):
        # while True:
            sleep(2)
            self.like()


bot = JinderBot()
bot.login()
sleep(10)
bot.swiperyesswiping()

#Log In
##Click Log
