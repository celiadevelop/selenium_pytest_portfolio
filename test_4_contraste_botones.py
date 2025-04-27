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

def test_contraste_en_botones(driver):
    # Abrir la web
    driver.get("https://ecommerce-playground.lambdatest.io/")
    time.sleep(2)  # Dar tiempo a que cargue

    # Buscar todos los botones principales
    botones = driver.find_elements(By.TAG_NAME, "button")

    botones_fallidos = []

    for boton in botones:
        color = boton.value_of_css_property("color")  # texto
        background = boton.value_of_css_property("background-color")  # fondo

        # Extraer los valores rgb
        color_rgb = [int(x) for x in color.replace('rgba(', '').replace('rgb(', '').replace(')', '').split(',')[:3]]
        background_rgb = [int(x) for x in background.replace('rgba(', '').replace('rgb(', '').replace(')', '').split(',')[:3]]

        # Función rápida para calcular brillo relativo
        def luminancia(rgb):
            r, g, b = [x/255.0 for x in rgb]
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        luminancia_texto = luminancia(color_rgb)
        luminancia_fondo = luminancia(background_rgb)

        # Calcular ratio de contraste
        contraste = (luminancia_fondo + 0.05) / (luminancia_texto + 0.05)
        if contraste < 1:
            contraste = 1 / contraste

        # Según WCAG AA normal debe ser mínimo 4.5:1
        if contraste < 4.5:
            botones_fallidos.append(boton)

    assert len(botones_fallidos) == 0, f"⚠️ Se encontraron {len(botones_fallidos)} botones con bajo contraste."

    print(f"✅ Test completado: Todos los botones principales tienen contraste suficiente. Total botones revisados: {len(botones)}")
