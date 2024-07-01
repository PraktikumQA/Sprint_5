from selenium.webdriver.common.by import By


class Locators:
# Page
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # Кнопка личного кабинета
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # Кнопка оформления заказа
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") # Кнопка перехода к конструктору
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # Лого страницы

# Constructor
    BUNS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]") # Кнопка раздела «Булки»
    SAUCES_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]") # Кнопка раздела «Соусы»
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]") # Кнопка раздела «Начинки»

#   Authentication

    AUTH_EMAIL_INPUT = (By.XPATH, "html/body/div/div/main/div/form/fieldset/div/div/input[1]") # Поле ввода email на странице авторизации
    AUTH_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") # Поле ввода пароля на странице авторизации
    AUTH_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка «Войти» на странице авторизации
    LOGIN_FROM_AUTH_FORM_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") # Кнопка «Войти» на странице регистрации
    LOGIN_FROM_PASSWORD_RECOVERY_FORM_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") # Кнопка «Войти» на странице восстановления пароля
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # Кнопка «Восстановить пароль» на странице восстановления пароля

#   Registration
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']") # Кнопка «Зарегистрироваться» на странице авторизации
    REGISTRATION_CONFORMATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка «Зарегистрироваться» на странице регистрации
    REGISTRATION_NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]") # Поле ввода имени на странице регистрации
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]") # Поле ввода email на странице регистрации
    REGISTRATION_PASSWORD_INPUT = (By.NAME, "Пароль") # Поле ввода пароля на странице регистрации

#   Personal account
    LOGOUT_BUTTON = (By.XPATH, "//button[(text()='Выход')]") # Кнопка выхода из аккаунта
