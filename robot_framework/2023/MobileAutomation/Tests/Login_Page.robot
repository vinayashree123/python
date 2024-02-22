*** Settings ***
Library  AppiumLibrary

*** Variables ***
&{User1_details}    email=vinayashreenaganuri5@gmail.com    password=Veena@123
${Login_Email_Field}
${Login_Password_Field}
${Login_Submit_Buton}

*** Test Cases ***
Amazon Home page
    open application  http://127.0.0.1:4724/wd/hub   automationName=UiAutomator2  platformName=Android  deviceName=chef_sprout    appPackage=in.amazon.mShop.android.shopping    appActivity=com.amazon.mShop.android.home.PublicUrlActivity
    wait until element is visible  //android.widget.ImageView[@content-desc="Select English"]
    click element    //android.widget.ImageView[@content-desc="Select English"]
    click element   in.amazon.mShop.android.shopping:id/continue_button
