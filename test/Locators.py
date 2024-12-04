from selenium.webdriver.common.by import By

class Locators:

    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    EMAIL = (By.XPATH, ".//input[@name='name']")
    PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ' and @class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    LINK_LOGIN = (By.CLASS_NAME, 'Auth_link__1fOlj')
    PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href='/account']")
    LOGIN_BUTTON_IN_PAGE_REGISTRATION = (By.XPATH, ".//a[@class='Auth_link__1fOlj']")
    LINK_REGISTRATION = (By.XPATH, ".//a[@href='/register']")
    LINK_FORGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")
    LOGIN_BUTTON_ON_MAIN_PAGE = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    BUTTON_EXIT = (By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    BUNS = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLINGS = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    CONSTRUCTOR = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2']")
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")
    NAME_IN_REGISTRATION = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_IN_REGISTRATION = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_IN_REGISTRATION = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REGISTRATION_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")