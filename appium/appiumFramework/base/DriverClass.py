from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '10',
            'deviceName': 'ZF6224GFW3',
            'app': r'C:\Users\vnaganur\Downloads\Android_Demo_App.apk',
            'appPackage': 'com.code2lead.kwad',
            'appActivity': 'com.code2lead.kwad.MainActivity'
        }

        driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)

        return driver
