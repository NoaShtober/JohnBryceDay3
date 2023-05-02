from PageObject.Pages.LoginPage import loginPage
from PageObject.Pages.WelcomePage import welcomePage
from PageObject.Tests.PageObjectBase import pageObjectBase

base = pageObjectBase()

driver = base.selenium_start("https://www.saucedemo.com/")
login_page = loginPage(driver)
login_page.login("standard_user", "secret_sauce")

welcome_page = welcomePage(driver)
prices = welcome_page.Welcome()

for price in prices:
    print(price.text)

assert prices[0].text == "$9.99"

base.selenium_end(driver)
