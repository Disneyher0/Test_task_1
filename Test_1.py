from selene.support.shared import browser
from selene import be, have
import pytest
browser.config.hold_browser_open = True

def test_mail():
    browser.open('https://google.com/ ')
    browser.element('[name="q"]').should(be.blank).type('mail').press_enter()
    browser.element('[id="search"]').should(have.text('Войти в электронную почту '))
    browser.element('[href="https://account.mail.ru/login"]').click()
    browser.element('[name="username"]').type('sssergey3344@mail.ru')
    browser.element('[data-test-id="next-button"]').click()
    browser.element('[name="password"]').type('jjaai11^DRYC')
    browser.element('[data-test-id="submit-button"]').click()
    browser.element('[data-testid="whiteline-account"]').click()
    browser.element('[href="https://id.mail.ru/security"]').click()
    browser.element('[data-test-id="navigation-menu-header"]').should(have.text('sssergey3344@mail.ru'))


