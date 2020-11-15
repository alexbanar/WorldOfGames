import sys
import time
from selenium import webdriver

def test_scores_service(app_url):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # chrome_driver = webdriver.Chrome(chrome_options=options, executable_path=r'.\\chromedriver.exe')

    global chrome_driver
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    options.add_argument("--window-size=480,320")
    chrome_driver = webdriver.Chrome(options=options, executable_path='.\\chromedriver.exe')
    chrome_driver.get(app_url)
    chrome_driver.set_window_size(480,320)
    chrome_driver.implicitly_wait(10)
    main_scores = int(chrome_driver.find_element_by_id("score").text)
    time.sleep(20)
    chrome_driver.quit();
    if main_scores >= 10 and main_scores <= 1000:
        return True
    else:
        return False

def main_function():
    app_url = "http://127.0.0.1:8777"
    scores_num_between_0_1000 = test_scores_service(app_url)

    if scores_num_between_0_1000:
        OS_exit_code = 0
        print("RESULT: [TEST SUCCESS]")
    else:
        OS_exit_code = -1
        print("RESULT: [TEST FAILURE]")
    
    return OS_exit_code

main_function()
#rc = main_function(sys.argv[1:])
#sys.exit(main_function())
