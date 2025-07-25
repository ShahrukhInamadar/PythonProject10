import logging
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s")
logger = logging.getLogger(__name__)

class BasePage():
  def __init__(self, driver, timeout=10):
    self.driver = driver
    self.timeout = timeout
    self.wait = WebDriverWait(self.driver, self.timeout)


  def _handle_exception(self, error_message, exception):
    logger.error(f"{error_message}:{str(exception)}")


  def do_click(self, locator):
    try:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info(f"Click on the element {locator}")
    except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
       self._handle_exception("error in click element", e)
       return e


  def do_send_keys(self, locator, text):
    try:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
        logger.info(f"Click on the element {locator}")
    except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
        self._handle_exception("error in enter element", e)
        return e

  def get_the_element(self, locator):
      try:
          element = self.wait.until(EC.element_to_be_clickable(locator))
          return element.text
      except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
          self._handle_exception("error in get_the_element", e)
          return None