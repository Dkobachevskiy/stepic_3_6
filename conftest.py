import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Choose language"
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs',
        {'intl.accept_languages': user_language}
    )
    if user_language:
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
        time.sleep(30)
    else:
        raise pytest.UsageError("please choose --language from list: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")
    print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()
