from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys

display = Display(visible=0, size=(1024, 768))
display.start()

print 'start use webdriver firefox'
driver = webdriver.Firefox()
print 'start connect python'
driver.get("http://www.python.org")
assert "Python" in driver.title
print driver.title
elem = driver.find_element_by_name("q")
print 'find q'
elem.send_keys("pycon")
print 'send pycon'
elem.send_keys(Keys.RETURN)
print 'send enter'
assert "No results found." not in driver.page_source
print 'will close'
driver.close()

print 'end'
