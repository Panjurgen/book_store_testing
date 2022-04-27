import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

# ----------------------------------------------------------------------------------------------------------
# # Shop: отображение страницы товара
# #
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
#
# myaccount = driver.find_element_by_css_selector("#menu-item-50>a")
# myaccount.click()
#
# username = driver.find_element_by_id("username")
# username.send_keys("mars@bk.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("CsGEddSW5345")
#
# login = driver.find_element_by_tag_name('[name="login"]')
# login.click()
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# # 4. Откройте книгу "HTML 5 Forms"
# html5 = driver.find_element_by_tag_name('[title="Mastering HTML5 Forms"]')
# html5.click()
# # 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
#
# product_title = driver.find_element_by_class_name("product_title")
# product_title_text = product_title.text
# print(product_title_text)
# assert "HTML5 Forms" in product_title_text

# ----------------------------------------------------------------------------------------------------------
# # Shop: количество товаров в категории
# #
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
# myaccount = driver.find_element_by_css_selector("#menu-item-50>a")
# myaccount.click()
# username = driver.find_element_by_id("username")
# username.send_keys("mars@bk.com")
# password = driver.find_element_by_id("password")
# password.send_keys("CsGEddSW5345")
# login = driver.find_element_by_tag_name('[name="login"]')
# login.click()
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# # 4. Откройте категорию "HTML"
# html = driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
# html.click()
# # 5. Добавьте тест, что отображается три товара
# tovars = driver.find_elements_by_css_selector(".products > .product")
# if len(tovars) == 3: # конструкция для проверки кол-ва товаров
#     print("Отображается 3 товара") # len здесь посчитает количество элементов, найденных при помощи find_elements
# else:
#     print("Ошибка. Количество товаров: " + str(len(tovars)))

# ----------------------------------------------------------------------------------------------------------
# # Shop: сортировка товаров
# #
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
# myaccount = driver.find_element_by_css_selector("#menu-item-50>a")
# myaccount.click()
# username = driver.find_element_by_id("username")
# username.send_keys("mars@bk.com")
# password = driver.find_element_by_id("password")
# password.send_keys("CsGEddSW5345")
# login = driver.find_element_by_tag_name('[name="login"]')
# login.click()
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# # • Используйте проверку по value
#
# selected = driver.find_element_by_tag_name('[value="menu_order"]')
# selected_value = selected.get_attribute("selected")
# print("В селекторе выбран вариант сортировки по умолчанию: ", selected_value)
# if selected_value is not None:
#     print("Все ок")
# else:
#     print("Выбрано неверное значение")
#
# # 5. Отсортируйте товары по цене от большей к меньшей
# # • в селекторах используйте класс Select
#
# sorttovar = driver.find_element_by_class_name("orderby")
# select = Select(sorttovar)
# select.select_by_index(5)
#
# # 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# orderby = driver.find_element_by_css_selector('.orderby > [value="price-desc"]')
# # 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# # • Используйте проверку по value
# #
# selected_orderby = orderby.get_attribute("selected")
# print("В селекторе выбран вариант сортировки по high to low: ", selected_orderby)
# if selected_orderby is not None:
#     print("Все ок")
# else:
#     print("Выбрано неверное значение")

# ----------------------------------------------------------------------------------------------------------
# # Shop: отображение, скидка товара
# #
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
# myaccount = driver.find_element_by_css_selector("#menu-item-50>a")
# myaccount.click()
# username = driver.find_element_by_id("username")
# username.send_keys("mars@bk.com")
# password = driver.find_element_by_id("password")
# password.send_keys("CsGEddSW5345")
# login = driver.find_element_by_tag_name('[name="login"]')
# login.click()
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# # 4. Откройте книгу "Android Quick Start Guide"
# android = driver.find_element_by_tag_name('[title="Android Quick Start Guide"]')
# android.click()
# # 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# oldprise = driver.find_element_by_css_selector("del>span")
# oldprisegettext = oldprise.text
# print("Старая цена: ", oldprisegettext)
# assert "₹600.00" in oldprisegettext
#
# # 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# newprise = driver.find_element_by_css_selector("ins>span")
# newprisegettext = newprise.text
# print("Новая цена: ", newprisegettext)
# assert "₹450.00" in newprisegettext
#
# # 7. Добавьте явное ожидание и нажмите на обложку книги
# # • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# obl = WebDriverWait(driver,20).until(
#     EC.element_to_be_clickable((By.TAG_NAME, '[title="Android Quick Start Guide"]')))
#
# image = driver.find_element_by_tag_name('[title="Android Quick Start Guide"]')
# image.click()
# # 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
#
# pp_close = WebDriverWait(driver,20).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
#
# pp_close = driver.find_element_by_class_name('pp_close')
# pp_close.click()

# ----------------------------------------------------------------------------------------------------------
# # Shop: проверка цены в корзине
# #
# # 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop"
# shopbtn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shopbtn.click()
# # 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# booktobasket = driver.find_element_by_tag_name('[data-product_id="182"]')
# booktobasket.click()
# # 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# # • Используйте для проверки assert
# time.sleep(3)
# cartcontents = driver.find_element_by_class_name("cartcontents")
# cartcontentstext = cartcontents.text
# print("Всего товаров в корзине: ", cartcontentstext)
# assert "1 Item" in cartcontentstext
# cost = driver.find_element_by_css_selector("a > .amount")
# costtext = cost.text
# print("Стоимость товаров в корзине: ", costtext)
# assert "₹180.00" in costtext
# # 5. Перейдите в корзину
# shoppingcart = driver.find_element_by_tag_name('[title="View your shopping cart"]')
# shoppingcart.click()
# # 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# subtotal = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]>span'), "₹180.00"))
# subtotal = driver.find_element_by_css_selector('[data-title="Subtotal"]>span')
# subtotaltext = subtotal.text
# print("Subtotal: ", subtotaltext)
# # 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# total = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'td>strong>span'), "₹189.00"))
# total = driver.find_element_by_css_selector('td>strong>span')
# totaltext = total.text
# print("Total: ", totaltext)
# # # если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# # # если все книги будут out of stock - тогда пропустите это и следующие два задания

# # ----------------------------------------------------------------------------------------------------------
# # Shop: работа в корзине
# #
# # Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# # 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop"
# shopbtn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shopbtn.click()
# # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# # • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# # • После добавления 1-й книги добавьте sleep
# driver.execute_script("window.scrollBy(0,300);")
# booktobasket = driver.find_element_by_tag_name('[data-product_id="182"]')
# booktobasket.click()
# time.sleep(3)
# booktobasket2 = driver.find_element_by_tag_name('[data-product_id="180"]')
# booktobasket2.click()
# # 4. Перейдите в корзину
# shoppingcart = driver.find_element_by_tag_name('[title="View your shopping cart"]')
# shoppingcart.click()
# # 5. Удалите первую книгу
# # • Перед удалением добавьте sleep
# time.sleep(3)
# bookdel = driver.find_element_by_tag_name('[data-product_id="182"]')
# bookdel.click()
# # 6. Нажмите на Undo (отмена удаления)
#
# undobtn = WebDriverWait(driver,20).until(
#      EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.woocommerce-message > a')))
# undo = driver.find_element_by_css_selector('div.woocommerce-message > a')
# undo.click()
# # 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# # • Предварительно очистите поле с помощью локатор_поля.clear()
# time.sleep(3)
# quantity = driver.find_element_by_css_selector('tr:nth-child(1) > td.product-quantity > div > input')
# quantity.clear()
# time.sleep(3)
# quantity.send_keys(3)
#
# # 8. Нажмите на кнопку "UPDATE BASKET"
# update = driver.find_element_by_tag_name('[value="Update Basket"]')
# update.click()
#
# # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
#
# valueqantity = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
# valueqantityvalue = valueqantity.get_attribute('value')
# print("Количество книг: ", valueqantityvalue)
# assert "3" in valueqantityvalue
# # 10. Нажмите на кнопку "APPLY COUPON"
# # • Перед нажатимем добавьте sleep
# time.sleep(3)
# apply = driver.find_element_by_tag_name('[name="apply_coupon"]')
# apply.click()
# # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# # # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
#
# message = driver.find_element_by_css_selector('div.woocommerce > ul > li')
# textmessage = message.text
# print(textmessage)
# assert "Please enter a coupon code." in textmessage


# ----------------------------------------------------------------------------------------------------------
# Shop: покупка товара
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shopbtn = driver.find_element_by_css_selector("#menu-item-40 > a")
shopbtn.click()
driver.execute_script("window.scrollBy(0,300);")
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
booktobasket = driver.find_element_by_tag_name('[data-product_id="182"]')
booktobasket.click()
# 4. Перейдите в корзину
shoppingcart = driver.find_element_by_tag_name('[title="View your shopping cart"]')
shoppingcart.click()
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание

checkoutbtn = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.wc-proceed-to-checkout > a')))
checkoutbtn.click()
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
driver.implicitly_wait(6)
first_name = driver.find_element_by_id('billing_first_name')
first_name.send_keys("Yuriy")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Yudin")
email = driver.find_element_by_id("billing_email")
email.send_keys("mars@bk.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("8989464221")

# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже



adress = driver.find_element_by_id("billing_address_1")
adress.send_keys("mendelleva 10")
city = driver.find_element_by_id("billing_city")
city.send_keys("Tomsk")
state = driver.find_element_by_id("billing_state")
state.send_keys("Oblast")
postkode = driver.find_element_by_id("billing_postcode")
postkode.send_keys("656565")



# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
cp = driver.find_element_by_id("payment_method_cheque")
cp.click()
# 8. Нажмите PLACE ORDER
place_order = driver.find_element_by_id("place_order")
place_order.click()
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
message = WebDriverWait(driver,20).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.woocommerce > p.woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
metod = WebDriverWait(driver,20).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.shop_table.order_details > tfoot > tr:nth-child(3) > td'), "Check Payments"))

time.sleep(4)
# driver.quit()