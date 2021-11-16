# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["deviceName"] = "SM_G935S"
caps["appPakage"] = "com.shouwuapp.mall"
caps["appActivity"] = ".business.SwMainActivity"
caps["resetKeyboard"] = True
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
class start_sumsung_shouwu():
    TouchAction(driver).tap(x=937, y=1823).perform()
    el2 = driver.find_element_by_id("com.shouwuapp.mall:id/id_user_avator")
    el2.click()
    time.sleep(1)
    el3 = driver.find_element_by_id("com.shouwuapp.mall:id/id_ed_phone")
    el3.send_keys("16621010110")
    time.sleep(1)
    el4 = driver.find_element_by_id("com.shouwuapp.mall:id/id_ed_verification_code")
    el4.send_keys("9876")
    time.sleep(1)
    el5 = driver.find_element_by_id("com.shouwuapp.mall:id/id_btn_confirm_check")
    el5.click()
    time.sleep(1)
    el6 = driver.find_element_by_id("com.shouwuapp.mall:id/id_btn_submit")
    el6.click()
    #用户从首页到点击头像登录
    time.sleep(1)
    TouchAction(driver).tap(x=134, y=1827).perform() #点击首页tab
    time.sleep(1)
    #下头这个滑动需要多加几个move_to...
    TouchAction(driver).press(x=1024, y=363).move_to(x=1024, y=888).move_to(x=1024, y=1383).move_to(x=1024, y=1683).release().perform()  #press按住元素 move_to移动至坐标release释放手指perform（表同时操作）
    time.sleep(2)
    #返回首页，并刷新页面
    xpath_top5 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView'
    el_top5 = driver.find_element_by_xpath(xpath_top5).text
    print(el_top5)
    driver.quit()
    #223334455
start_sumsung = start_sumsung_shouwu()
