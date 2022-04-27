import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0,600);")
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selenium_ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3")
selenium_ruby.click()
# 4. Нажмите на вкладку "REVIEWS"
reviews = driver.find_element_by_tag_name('[href="#tab-reviews"]')
reviews.click()
# 5. Поставьте 5 звёзд
star5 = driver.find_element_by_class_name('star-5')
star5.click()
# 6. Заполните поле "Review" сообщением: "Nice book!"
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice booooook!")
# 7. Заполните поле "Name"
author = driver.find_element_by_id("author")
author.send_keys("Marsh Mellou")
# 8. Заполните "Email"
email = driver.find_element_by_id("email")
email.send_keys("marshmellou@mail.com")
# 9. Нажмите на кнопку "SUBMIT"
submit = driver.find_element_by_id("submit")
submit.click()
time.sleep(6)
driver.quit() # команда quit() – нужна для закрытия всех вкладок и завершения процесса webdriver

