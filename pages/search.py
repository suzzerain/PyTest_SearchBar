# Импорт библиотек
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Класс DuckDuckGoSearchPage
class DuckDuckGoSearchPage:
    # Тело класса
    URL = 'https://www.duckduckgo.com' # URL страницы
    SEARCH_INPUT = (By.ID, "searchbox_input") # Локатор строки поиска

    # Конструктор класса
    def __init__(self, browser):
        self.browser = browser # Объект браузера

    # Метод для загрузки страницы поиска
    def load(self):
        self.browser.get(self.URL) # вызов метода .get браузера для открытия страницы

    # Метод для выполнения поискового запроса
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN) # Отправка фразы
