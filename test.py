from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def email_auth(driver):
    """Функция авторизации на mail.ru"""
    
    url = "https://mail.ru/?from=logout"
    login = "kirya.kulikov.20@bk.ru"
    password = "league_econom_1"
    
    driver.get(url)

    time.sleep(1)
    
    enter_login = driver.find_element_by_id("mailbox:login-input")
    enter_login.send_keys(login)
    driver.find_element_by_id("mailbox:submit-button").click()

    time.sleep(1)
    
    enter_password = driver.find_element_by_id("mailbox:password-input")
    enter_password.send_keys(password)
    driver.find_element_by_id("mailbox:submit-button").click()
    
def email_send(driver):
    """Функция заполнения и отправки формы письма"""
    
    driver.get("https://e.mail.ru/compose/")
    
    time.sleep(1)
    
    destination_emails = driver.find_element_by_xpath("//input[@class='container--H9L5q size_s_compressed--2c-eV']")
    destination_emails.send_keys("idedov@at-consulting.ru" + " ")
    
    destination_emails = driver.find_element_by_xpath("//input[@class='container--H9L5q size_s_compressed--2c-eV']")
    destination_emails.send_keys("nbykanov@at-consulting.ru")

    
    email_text = driver.find_element_by_xpath("//input[@class='container--H9L5q size_s_compressed--2c-eV'][@name='Subject']")
    email_text.send_keys("Куликов Кирилл Геннадиевич" + " ")
    email_text.send_keys("https://github.com/frenchy156/Test_Task")

    time.sleep(3)
    
    driver.find_element_by_xpath("//span[@class='button2__wrapper'][@tabindex='570']").click()
    driver.find_element_by_xpath("//button[@class='c2185 c2160 c2196 c2171 c21104 c2180']").click()

if __name__ == "__main__" :
    driver_ch = webdriver.Chrome()
    
    email_auth(driver_ch)
    
    time.sleep(3)

    email_send(driver_ch)
    
