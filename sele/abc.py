#import webdriver from selenium
from selenium import webdriver

#importing By to get elements from website(HTML)
from selenium.webdriver.common.by import By

#To add delay for slow connections
import time

# To take encrypted input of PASSWORD
from getpass import getpass

#Initiate crome driver
browser = webdriver.Chrome()

#Open CodeForces Login page
browser.get("https://codeforces.com/enter?back=%2F")

#Take input of Username
usr = input('Enter your Username  ')

#add 1 sec delay for slow connections
time.sleep(1)

#finding username element
username = browser.find_element(By.ID, 'handleOrEmail')

#send username to site
username.send_keys(usr)
#find password element
passwo = browser.find_element(By.ID, 'password')

#send Password through get pass
passwo.send_keys(getpass('Enter your Password '))

#click on submit button
browser.find_element(By.CLASS_NAME, 'submit').click()

# time.sleep(2)

#Redirecting to submit page after authntication
browser.get('https://codeforces.com/problemset/submit')

#add 2 sec delay for slow connections
time.sleep(2)

#finding element to enter problem code
p_code = browser.find_element(By.NAME, 'submittedProblemCode')

#taking input of problem code
pro_code = input('Enter Problem Code:-')

#sending problem code to browser
p_code.send_keys(pro_code)

#check toggle editor to enable text box
browser.find_element(By.ID, 'toggleEditorCheckbox').click()

#asking user for solution of problem
solution = input("Paste Solution ")

#finding text area 
code = browser.find_element(By.ID, 'sourceCodeTextarea')

#send solution to textt area
code.send_keys(solution)

#click on submit button
browser.find_element(By.CLASS_NAME, 'submit').click()

#print "Submitted Succesfully" after the program is completed
print("Submitted Succesfully")
