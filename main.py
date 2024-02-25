from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from time import sleep

try:

    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    driver.get("https://www.ai27.com/") 

    sleep(3)

    #Search full_name, email, email , company, message ... submit
    inputNombre = driver.find_element(By.NAME, "full_name")
    inputNombre.send_keys('Jorge Salgado')

    inputemail = driver.find_element(By.NAME, "email")
    inputemail.send_keys('salgado.jm.91@gmail.com') 

    inputcompany = driver.find_element(By.NAME, "company")
    inputcompany.send_keys('candidato') 

    inputmsn = driver.find_element(By.NAME, "message")
    inputmsn.send_keys('ejemplo selenium con python local')

    sleep(3)

    inputmsn.submit()  

finally:
    driver.quit()
    
