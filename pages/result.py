# Импортируется необходимый класс By из библиотеки Selenium.:
from selenium.webdriver.common.by import By
# Определение класса DuckDuckGoResultPage
class DuckDuckGoResultPage:
    # Тело класса

    # статическая переменная, содержащая информацию о методе поиска элементов
    SEARCH_RESULTS = (By.CSS_SELECTOR, "li[data-layout='organic']")
    # статическая переменная, содержащая информацию о методе поиска элементов поисковой строки
    SEARCH_INPUT = (By.ID, 'search_form_input')

    @classmethod
    #Статический метод PHRASE_RESULTS()

    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//li[@data-layout='organic']//a[contains(@href,'{phrase}')]"
        return (By.XPATH, xpath)
    # Конструктор класса
    def __init__(self, browser):
        self.browser = browser

    # Метод, который находит все элементы результатов поиска на странице и возвращает кол-во
    def search_results_count(self):
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)
        return len(search_results)
    # Метод находит все ссылки результатов поиска, содержащих пользовательский запрос
    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)

    # Метод, который находит элемент поисковой строки на странице
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')