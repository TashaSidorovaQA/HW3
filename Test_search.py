from selene import browser, have

def test_search_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('[id="search-result"]').should(have.text('Курсы тестировщиков'))


def test_search_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('gjerдigeg[og').press_enter()
    browser.element('[id="search-result"]').should(have.text('По запросу gjerigeg[og ничего не найдено'))