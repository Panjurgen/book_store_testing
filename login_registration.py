import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

# # Registration_login: регистрация аккаунта
# #
# # 1. Откройте http://practice.automationtesting.in/
# driver.get('http://practice.automationtesting.in/')
# # 2. Нажмите на вкладку "My Account Menu"
# myaccount = driver.find_element_by_css_selector("#menu-item-50>a")
# myaccount.click()
# # 3. В разделе "Register", введите email для регистрации
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys('mars@bk.com')
# # 4. В разделе "Register", введите пароль для регистрации
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("CsGEddSW")
# time.sleep(2)
# reg_password.send_keys("5345")
# # • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# # • почту и пароль сохраните, потребуюутся в дальнейшем
# # 5. Нажмите на кнопку "Register"
#
# time.sleep(2)
#
# reg = driver.find_element_by_tag_name('[name="register"]')
# reg.click()
#
# time.sleep(10)
# driver.quit()


# Registration_login: логин в систему
#
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2. Нажмите на вкладку "My Account Menu"
myaccount = driver.find_element_by_css_selector("#menu-item-50>a")
myaccount.click()
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
username = driver.find_element_by_id("username")
username.send_keys("mars@bk.com")
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
password = driver.find_element_by_id("password")
password.send_keys("CsGEddSW5345")
# 5. Нажмите на кнопку "Login"
login = driver.find_element_by_tag_name('[name="login"]')
login.click()
# 6. Добавьте проверку, что на странице есть элемент "Logout"
# <a href="http://practice.automationtesting.in/my-account/customer-logout/">Logout</a>
logout = driver.find_element_by_css_selector("#page-36 > div > div.woocommerce > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")
logout_get_text = logout.text
print(logout_get_text)
assert "Logout" in logout_get_text