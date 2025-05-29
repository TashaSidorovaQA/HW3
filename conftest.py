@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_width = 800
    browser.config.window_height = 600
    yield
    browser.quit()