from selenium import webdriver
from getpass import getpass

#install selenium using 
#pip install selenium
#in the terminal


# website credentials for login 
username = ""  # Replace with your username
password = ""  # Replace with your password

# To open the browser
browser = webdriver.Chrome()

# paste the url of the website you want to login to in the below line
browser.get("https://www.example.com")# Replace with your URL

# To Login
try:
    #inspect the username field and get the name or id and replace it with the name or id in the below code

    nameElem = browser.find_element("name", "username")
    nameElem.send_keys(username)
    #inspect the password field and get the name or id and replace it with the name or id in the below code
    passElem = browser.find_element("name", "password")
    passElem.send_keys(password)
    #inspect the login button and get the name or id and replace it with the name or id in the below code
    login = browser.find_element("id", 'login')
    login.click()

    input("Press Enter to exit...")
except Exception as e:
    print("An error occurred:", e)
finally:
    browser.quit()
