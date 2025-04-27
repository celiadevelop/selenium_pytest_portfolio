# test_2_busqueda_producto.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_busqueda_producto(driver):
    # Abrir la web
    driver.get("https://ecommerce-playground.lambdatest.io/")

    # Buscar el campo de búsqueda
    search_input = driver.find_element(By.NAME, "search")
    search_input.send_keys("iPhone")

    # Hacer clic en el icono de búsqueda
    search_button = driver.find_element(By.CLASS_NAME, "type-text")
    search_button.click()

    # Esperar que carguen los resultados
    time.sleep(2)

    # Verificar que se mostraron productos
    productos = driver.find_elements(By.CLASS_NAME, "product-thumb")
    assert len(productos) > 0, "No se encontraron productos"

    print(f"✅ Test completado: se encontraron {len(productos)} productos.")



