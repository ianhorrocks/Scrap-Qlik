import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_web(url):
    
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.set_window_size(1600, 1200)  # Relacion Aspecto de la pantalla, ajustar si es necesario
    #driver.execute_script("document.body.style.zoom='80%'") # Establece el zoom a 80%
    return driver

def login(driver, username, password):
    
    wait = WebDriverWait(driver, 10) # Cuando esten listos los elementos para la carga, se les pasara las credenciales y le manda click
    input_user = wait.until(EC.visibility_of_element_located((By.XPATH, '//main//input[@name="email"]')))
    input_user.send_keys(username)
    input_pass = wait.until(EC.visibility_of_element_located((By.XPATH, '//main//input[@name="password"]')))
    input_pass.send_keys(password)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//main//button[@name="submit"]')))
    login_button.click()

    time.sleep(18)

def take_screenshot(driver):
    
    wait = WebDriverWait(driver, 10)
    qs_page_container = wait.until(EC.visibility_of_element_located((By.ID, "qs-page-container")))

    today_date = datetime.now().strftime("%d-%b")
    screenshot_name = f"Cumpleaños al {today_date}.png" 
    qs_page_container.screenshot(screenshot_name)

def main():
    URL = 'https://it-maker.us.qlikcloud.com/sense/app/0b23097a-11c9-41b3-aac2-8ab9b48b0822/sheet/4df3943b-0560-440d-995a-2944353cdb1d/state/analysis' # Enlace a la hoja
    username = "ian.horrocks@itmaker.com.ar" 
    password = open('password.txt').readline().strip() #Crear un txt con la contra dentro
    driver = get_web(URL)
    
    try:
        login(driver, username, password)
        take_screenshot(driver)
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()