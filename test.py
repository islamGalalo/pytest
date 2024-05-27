#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWebsite:
    def test_one(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://automationexercise.com/')
        driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
        wait = WebDriverWait(driver, 10)
  