import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_imagenes_con_alt(driver):
    # Abrir la web
    driver.get("https://ecommerce-playground.lambdatest.io/")

    # Buscar todas las imágenes
    imagenes = driver.find_elements(By.TAG_NAME, "img")

    # Verificar que cada imagen tiene atributo 'alt' no vacío
    imagenes_sin_alt = []

    for img in imagenes:
        alt_text = img.get_attribute("alt")
        if alt_text is None or alt_text.strip() == "":
            imagenes_sin_alt.append(img)

    # Assert final
    assert len(imagenes_sin_alt) == 0, f"⚠️ Se encontraron {len(imagenes_sin_alt)} imágenes sin atributo alt."

    print(f"✅ Test completado: Todas las imágenes tienen atributo 'alt'. Total imágenes revisadas: {len(imagenes)}")
