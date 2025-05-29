@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_width = 1000
    browser.config.window_height = 900
    yield
    browser.quit()