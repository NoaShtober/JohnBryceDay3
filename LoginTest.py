from PageObject.Pages.LoginPage import loginPage
from PageObject.Tests.PageObjectBase import pageObjectBase

base = pageObjectBase()

driver = base.selenium_start("https://www.saucedemo.com/")
login_page = loginPage(driver)
login_page.login("standard_user", "secret_sauce")
base.selenium_end(driver)
