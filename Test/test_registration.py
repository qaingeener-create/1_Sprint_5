from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Генераторы логина и пароля
def generate_email():
    return f"test{random.randint(1000, 9999)}@example.com"

def generate_password():
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))

# Тесты
def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")

    # Ввод данных
    name_input = driver.find_element(By.NAME, "name")
    name_input.send_keys("Test Name")
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(generate_email())
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(generate_password())

    # Отправка формы
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    # Проверка успешной регистрации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profilePage")))

    driver.quit()

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/login")

    # Ввод данных
    login_email_input = driver.find_element(By.NAME, "loginEmail")
    login_email_input.send_keys(generate_email())
    login_password_input = driver.find_element(By.NAME, "loginPassword")
    login_password_input.send_keys(generate_password())

    # Отправка формы
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profilePage")))

    driver.quit()

def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/account/profile")

    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выйти']")))
    logout_button.click()

    # Проверка выхода из аккаунта
    WebDriverWait(driver, 10).until(EC.url_changes("https://stellarburgers.education-services.ru/account/profile"))

    driver.quit()
