from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time
import os


def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)



DRIVER_PATH = "\\Users\\hsass\\Desktop\\Trainng-Perl_Python\\chromedriver.exe"
PROFILE_PATH = r"C:\Users\hsass\AppData\Local\Google\Chrome\User Data\Default"

	
	
options = Options()
#options.headless = True
#options.add_argument("--headless")
#options.add_argument("--window-size=1920x1080")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--verbose')
#options.add_argument("user-data-dir=" + PROFILE_PATH)
options.add_experimental_option("prefs", {
    "download.default_directory": "<path_to_download_default_directory>",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})
#options.add_argument('--disable-gpu')
#options.add_argument('--disable-software-rasterizer')


x = 0

#while x < 5:


browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# download_dir = "<path_to_place_downloaded_file>"

# enable_download_headless(browser, download_dir)


#browser = webdriver.Chrome('\\Users\\hsass\\Desktop\\Trainng-Perl_Python\\chromedriver.exe')
#browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#browser.get('https://analytics.wipro.com/login.aspx')
browser.get('https://mywipro.wipro.com/')

# def Sign():

    # browser.find_element_by_id('signinButton-announce')

    # elem = browser.find_element_by_id('signinButton-announce')
    # elem.click()

    # email = browser.find_element_by_id('ap_email')
    # email.send_keys(' ')

    # password = browser.find_element_by_id('ap_password')
    # password.send_keys(' ')

    # SignIn = browser.find_element_by_id('signInSubmit')
    # SignIn.click()

# def Sign1():

    # browser.find_element_by_id('signinButton-announce')

    # elem = browser.find_element_by_id('signinButton-announce')
    # elem.click()

    # email = browser.find_element_by_id('ap_email')
    # email.send_keys(' ')

    # password = browser.find_element_by_id('ap_password')
    # password.send_keys(' ')

    # SignIn = browser.find_element_by_id('signInSubmit')
    # SignIn.click()
    # browser.execute_script("window.open('https://kdp.amazon.com/en_US/', 'new window')")
# Sign()


time.sleep(40)

def Action():
    
   #element = browser.find_element_by_css_selector("a.weighing sprite").click
   
#x_path /html/body/app-root/div/app-landing/div[1]/div/app-home/section/div[1]/app-favourite-apps/div/div/ul/li/div[1]/div[1]/button

	# element = browser.find_element_by_css_selector("body > app-root > div > app-landing > div.headerCls > div > app-home > section > div.pull-left.leftsection_main > app-favourite-apps > div > div > ul > li > div.mt10.col-xs-4.col-sm-4.col-md-4.col-lg-4.no_pad.fav_circle.animate_fav.icon_text_hover.fav_one > div.fav_main > button")
	# element.click()
	wait = WebDriverWait(browser, 10)
	browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
	#browser.manage().window().maximize();
	browser.get("https://analytics.wipro.com/reports.aspx")
	browser.implicitly_wait(10)
	browser.get("https://analytics.wipro.com/reports.aspx")
	#element = wait.until(EC.element_to_be_clickable((By.XPath, '//*[@id="liReportTiles"]')))
	
	soup = BeautifulSoup(browser.page_source)
	dict_from_json = json.loads(soup.find("body").text)
	element = browser.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div/div/div/div[3]/md-content[2]/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[6]')
	element.click()
	
	

# if (browser.current_url == 'https://analytics.wipro.com/reports.aspx'):
    # #Sign1()
    # Action()
	# x += 1
	
if (browser.current_url == 'https://mywipro.wipro.com/Home'):
    #Sign1()
    Action()