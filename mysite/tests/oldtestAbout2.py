from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import selenium
import selenium.webdriver.edge.options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MyRealTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = selenium.webdriver.edge.options.Options()
        MyRealTest.driver = selenium.webdriver.Edge(options=options)

    @classmethod
    def tearDownClass(cls):
        MyRealTest.driver.quit()
        super().tearDownClass()

    def test_about(self):
        driver = MyRealTest.driver
        driver.get( f"{self.live_server_url}/about" )
        elem = driver.find_element(By.CLASS_NAME, "username")
        self.assertTrue( elem.text == "Bob" )