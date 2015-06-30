import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time


class StringsInStrings(unittest.TestCase):
    def setUp(self):
        self.client = webdriver.Safari()
        self.worker = webdriver.Safari()

    def test_client_counter(self):
        client = self.client
        client.get("http://localhost:8081/client")
        worker = self.worker
        worker.get("http://localhost:8081/worker")

        self.assertIn("Client", client.title)
        self.assertIn("Worker", worker.title)

        substring = client.find_element_by_id("substring")
        substring.value = "dd"

        main_string = client.find_element_by_id("main_string")
        main_string.value = "dddd"

        client.find_element_by_id("start").click()

        time.sleep(40)

        result = client.find_element_by_id("result").value
        assert "dd=3" in result

    def tearDown(self):
        self.client.close()
        self.worker.close()


if __name__ == "__main__":
    unittest.main()
