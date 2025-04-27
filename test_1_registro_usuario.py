# test_1_registro_usuario.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    # Configurar el driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_registro_usuario(driver):
    # Ir a la página principal
    driver.get("https://ecommerce-playground.lambdatest.io")
    
    # Click en "My account" y luego en "Register"
    driver.find_element(By.LINK_TEXT, "My account").click()
    driver.find_element(By.LINK_TEXT, "Register").click()

    # Llenar formulario
    driver.find_element(By.ID, "input-firstname").send_keys("Test")
    driver.find_element(By.ID, "input-lastname").send_keys("User")
    driver.find_element(By.ID, "input-email").send_keys(f"testuser{int(time.time())}@example.com")
    driver.find_element(By.ID, "input-telephone").send_keys("123456789")
    driver.find_element(By.ID, "input-password").send_keys("Test@1234")
    driver.find_element(By.ID, "input-confirm").send_keys("Test@1234")

    # Aceptar política de privacidad
    label = driver.find_element(By.XPATH, "//label[@for='input-agree']")
    label.click()


    # Click en "Continue"
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    # Esperar a que aparezca el mensaje de éxito
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]"))
    )

    # Verificación del resultado
    assert success_message.is_displayed(), "El mensaje de éxito no apareció."


