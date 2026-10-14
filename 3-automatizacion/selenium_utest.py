from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

print("Iniciando pruebas")
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Acceso a la pagina 
    driver.get("https://www.utest.com/")
    print("Página principal cargada exitosamente.")
    time.sleep(3)

    # Botón "Join Now" 
    btn_join = driver.find_element(By.CLASS_NAME, "unauthenticated-nav-bar__sign-up")
    btn_join.click()
    time.sleep(3)

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
    
    time.sleep(3)
    print("Carga de pantalla de registro exitosa.")

    print("Llenando campos del formulario...")
    
    # Nombre
    input_firstname = driver.find_element(By.ID, "firstName")
    input_firstname.send_keys("Luis Alfonso")
    time.sleep(3)
    
    # Apellido
    input_lastname = driver.find_element(By.ID, "lastName")
    input_lastname.send_keys("Eguia Lis Dotor")
    time.sleep(3)
    
    # Correo electrónico
    input_email = driver.find_element(By.ID, "email")
    input_email.send_keys("eguialisdotor@gmail.com")
    time.sleep(3)

    # Fecha de Nacimiento
    select_month = Select(driver.find_element(By.ID, "birthMonth"))
    select_month.select_by_visible_text("August")
    time.sleep(2)

    select_day = Select(driver.find_element(By.ID, "birthDay"))
    select_day.select_by_value("5")
    time.sleep(2)

    select_year = Select(driver.find_element(By.ID, "birthYear"))
    select_year.select_by_visible_text("2002")
    time.sleep(3)

    # Terminos y Condiciones
    checkbox_terms = driver.find_element(By.ID, "termsAccepted")
    driver.execute_script("arguments[0].click();", checkbox_terms)
    time.sleep(2)
    
    checkbox_news = driver.find_element(By.ID, "newsletterOptIn")
    driver.execute_script("arguments[0].click();", checkbox_news)
    time.sleep(3)

    print("Llenado del formulario exitoso.")

    time.sleep(2)
    
    btn_create_account = driver.find_element(By.CLASS_NAME, "btn-create-account")
    btn_create_account.click()
    print("Botón 'Create Account' presionado exitosamente.")
    
    time.sleep(5)

except Exception as e:
    print("Ocurrió un error durante la ejecución de la prueba:", e)

finally:
    # Cerrar navegador
    print("Pruebas finalizadas exitosamente.")
    driver.quit()