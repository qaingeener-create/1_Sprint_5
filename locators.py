# Локаторы для страницы регистрации
REGISTRATION_FORM = (By.ID, "registrationForm")  # Форма регистрации
NAME_INPUT = (By.NAME, "name")  # Поле ввода имени
EMAIL_INPUT = (By.NAME, "email")  # Поле ввода email
PASSWORD_INPUT = (By.NAME, "password")  # Поле ввода пароля
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации

# Локаторы для страницы входа
LOGIN_FORM = (By.ID, "loginForm")  # Форма входа
LOGIN_EMAIL_INPUT = (By.NAME, "loginEmail")  # Поле ввода email для входа
LOGIN_PASSWORD_INPUT = (By.NAME, "loginPassword")  # Поле ввода пароля для входа
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа

# Локаторы для личного кабинета
PROFILE_PAGE = (By.ID, "profilePage")  # Страница личного кабинета
CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")  # Ссылка на конструктор
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка выхода из аккаунта

# Локаторы для конструктора
CONSTRUCTOR_PAGE = (By.ID, "constructorPage")  # Страница конструктора
BUNS_SECTION = (By.ID, "bunsSection")  # Раздел "Булки"
SAUCES_SECTION = (By.ID, "saucesSection")  # Раздел "Соусы"
FILLINGS_SECTION = (By.ID, "fillingsSection")  # Раздел "Начинки"
