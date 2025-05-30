import pytest
from selene import browser, be, have


def test_search_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('[id="search-result"]').should(have.text('Об этой странице'))


def test_search_negative():
    browser.open('https://ya.ru/')
    browser.element('[name="text"]').type('gjerдigeg[og').press_enter()
    browser.element('[id="search-result"]').should(have.text('Ничего не нашли'))