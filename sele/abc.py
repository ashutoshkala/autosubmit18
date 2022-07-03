from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from getpass import getpass
browser = webdriver.Chrome()
browser.get("https://codeforces.com/enter?back=%2F")
usr = input('Enter your Username  ')

time.sleep(1)
username = browser.find_element(By.ID, 'handleOrEmail')
username.send_keys(usr)
passwo = browser.find_element(By.ID, 'password')
passwo.send_keys(getpass('Enter your Password '))
browser.find_element(By.CLASS_NAME, 'submit').click()
time.sleep(2)
browser.get('https://codeforces.com/problemset/submit')
time.sleep(2)
p_code = browser.find_element(By.NAME, 'submittedProblemCode')
pro_code = input('Enter Problem Code:-')
p_code.send_keys(pro_code)
browser.find_element(By.ID, 'toggleEditorCheckbox').click()
solution = input("Paste Solution ")
code = browser.find_element(By.ID, 'sourceCodeTextarea')
code.send_keys(solution)
browser.find_element(By.CLASS_NAME, 'submit').click()

print("Submitted Succesfully")
