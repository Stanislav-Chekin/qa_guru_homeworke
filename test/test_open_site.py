import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """Фикстура: создаёт headless Chrome, возвращает его и закрывает после теста."""
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")

    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_selenium(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)

    assert "Selenium" in driver.title
    assert driver.current_url == url


def test_google(driver):
    url = "https://www.google.com/"
    driver.get(url)

    assert "Google" in driver.title
    assert driver.current_url == url


def test_github(driver):
    url = "https://github.com/"
    driver.get(url)

    assert "GitHub" in driver.title
    assert driver.current_url == url

