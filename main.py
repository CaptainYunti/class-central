from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from webdriver_manager.chrome import ChromeDriverManager
import os
import shutil


shutil.copytree(src="C:/Users/panie/HindiProject2", dst="./site")


# options = Options()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# driver.maximize_window()
