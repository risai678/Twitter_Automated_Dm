from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import random
import parameters
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



class MyClass():
    def __init__(self):

        self.id = parameters.userrr
        self.password = parameters.passs

        # loading chrome driver
        self.driver = webdriver.Chrome('./chromedriver_85')

    def csv_tolist(self):
        df = pd.read_csv('/home/webtunix/American23.csv')

        list2 = df['screen_name'].to_list()
        # print(list2)
        list3 = df['name'].to_list()
        
        return list2,list3
    

def login(self):
        driver=self.driver
        driver.get('https://twitter.com/login')
        sleep(0.5)
        driver.find_element_by_xpath("//input[contains(@name,'session[username_or_email]')]").send_keys(str(self.id))
        driver.find_element_by_xpath("//input[contains(@name,'session[password]')]").send_keys(str(self.password))
        sign_in_button = driver.find_element_by_xpath('//*[@role="button"]'
                                                      )
        sign_in_button.click()

    def message(self):
        driver = self.driver
        list11,list12=self.csv_tolist()
        send_count=2698
        for countt in list11[33754:]:
                try:

                    driver.get('https://twitter.com/messages/compose?')
                    sleep(5)
                    driver.find_element_by_xpath("//input[contains(@data-testid,'searchPeople')]").send_keys(str(countt))
                    counter=list11.index(countt)
                    print(counter)
                    sleep(3)
                    try:
                        namee=driver.find_element_by_xpath("//*[@class='css-901oao css-bfa6kz r-18jsvk2 r-1qd0xha r-a023e6 r-b88u0q r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']").text
                    except:
                        namee=driver.find_element_by_xpath("//*[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']").text
                    namee=namee.split(' ')
                    driver.find_element_by_xpath("//*[@class='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci']").click()
                    sleep(2)
                    driver.find_element_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-19u6a5r r-15ysp7h r-gafmid r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']").click()

                    sleep(8)

                    text1 = "Hi,"
                    text2="I represent the team at Webtunix AI. I wanted to discuss a possible collaboration in AI Solution for your Organization, which we deliver as per your requirement."
                    text3="Services:"
                    text4="Artificial Intelligence,Machine learning,Mobile App development,Website Development,Digital Marketing"
                    text5="Kindly share your contact details to discuss further if this interests you"

                    text6="Gagandeep Singh"
                    text7="+91-9872993778"
                    text8="gsingh@webtunix.com"
                    text9="www.webtunix.com"

                    kk=[text1,text2,text3,text4,text5]
                    kk2=[text6,text7,text8,text9]
                    # sleep(1)
                    # driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(link)
                    sleep(2)
                    driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerSendButton')]").click()
                    for k in kk:
                        driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(k)
                        driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(Keys.SHIFT + Keys.ENTER)

                        
                    driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(Keys.SHIFT + Keys.ENTER)

                    # driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(text4)
                    for l in kk2:
                        driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(l)
                        driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(Keys.SHIFT + Keys.ENTER)
                    send_count+=1
                    print(send_count,'==total_send')
                    time1 = random.randint(7,20)
                    sleep(time1)
                    driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerSendButton')]").click()
                    time2=random.randint(25,40)
                    sleep(time2)
                except:
                    pass





aa=MyClass()
# function for login
aa.login()
# function for message
aa.message()
