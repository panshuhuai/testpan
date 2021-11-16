from selenium import webdriver
import random
import time
from testpan import db_order_prodout


class Wed():
    def __init__(self,):
        self.browsers = webdriver.Chrome()
    def click_find_element(self,url,element):
        time.sleep(1)
        self.browsers.get(url=url)
        time.sleep(2)
        self.browsers.maximize_window() #窗口最大化
        time.sleep(1)
        #self.browsers.find_element_by_xpath(element).click()
        try:
            detaill_price_text = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/div[1]/div/span').text
            detaill_price = float(detaill_price_text[4:])
            if detaill_price != 1.99:
                print("商品价格异常")
            else:
                pass
        except:
            detaill_price = 0
            print("获取商品价格异常")
            pass
        return detaill_price
        #  暂时弹窗按钮元素找不到，暂时不知道如何解决 ，先缓缓
        # try:
        #     self.browsers.find_element_by_xpath('//*[@id="am-modal-container-1624695308197"]/div/div[2]/div/div/div/div/div[2]/div/a/span[1]').click()
        #     #点击弹出框中的 Buy Now按钮，跳转订单页
        # except:
        #     self.browsers.find_element_by_css_selector('#am-modal-container-1624695620509 > div > div.am-modal-wrap.modal_actionSheetModal__6YrfV.am-modal-wrap-popup > div > div > div > div > div.detailFooterBtn_btnContainerWrap__2qWLW > div > a').click()
        # time.sleep(2)
        # #获取商品价格，并验证金额是否和subtotal以及detaill页金额一致

    def check_Confirmation_element(self, url):
        self.browsers.get(url=url)
        time.sleep(1)
        self.browsers.maximize_window()
        #寻找元素，并将浏览器滑动到元素处
        target = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[11]/div[2]')
        self.browsers.execute_script("arguments[0].scrollIntoView();", target)
        try:
            time.sleep(1)
            pr_price_text = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[2]/div[3]/span').text
            pr_price = float(pr_price_text[1:])
            time.sleep(1)
            Package_subtotal_text =self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[3]/span[2]').text
            Package_subtotal = float(Package_subtotal_text[1:])
            time.sleep(1)
            Package_delivery_text = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[4]/span[2]').text
            Package_delivery_fee = float(Package_delivery_text[1:])
            Package_tax_fee_text = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[5]/span[2]').text
            Package_tax_fee = float(Package_tax_fee_text[1:])
        except:
            pr_price = 0
            Package_subtotal = 0
            Package_delivery_fee = 0
            Package_tax_fee = 0
            print("商品价格获取异常")
        time.sleep(1)
        try:
            Package_coupons = float(self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[6]/span[2]').text)[2:]
        except:
            print('Package_coupons,当前未检测到用户存在优惠劵，默认优惠为0元')
            Package_coupons = 0
        time.sleep(1)
        Package_total_text = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[7]/span[2]').text
        Package_total=float(Package_total_text[1:])
        User_total_text = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[7]/span[2]').text
        User_total=float(User_total_text[1:])
        time.sleep(0.5)
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[3]/div[1]/div/div/a/span').click()
        #进入地址页面，输入地址
        time.sleep(1)
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[1]/div[2]/input').send_keys('testtester')
        time.sleep(0.5)
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[3]/div[2]/input').send_keys('testtestertesttester')
        time.sleep(0.5)
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[4]/div/div[2]/input').send_keys('ALABAMA')
        time.sleep(0.5)
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[5]/div/div[2]/input').send_keys('Abbeville')
        time.sleep(0.5)
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[6]/div[2]/input').send_keys('22222')
        time.sleep(0.5)
        target = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[8]/div[2]/input')
        self.browsers.execute_script("arguments[0].scrollIntoView();", target)
        #移动浏览器到输入Email区域
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[7]/div[2]/input').send_keys('1333333333333')
        email_top = random.randrange(100,9000000000)
        email = str(email_top) + "@qq.com"
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/div[8]/div[2]/input').send_keys(email)
        time.sleep(0.5)
        self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/form/a/span').click()
        time.sleep(3)
        self.browsers.find_element_by_xpath('//div/div[2]/div/div/button').click()
        # WebDriverWait(self.browsers,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="am-modal-container-1624863499069"]/div/div[2]/div/div/button/spa')))

        # 寻找元素，并将浏览器滑动到元素处
        target = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[11]/div[2]/div/textarea')
        self.browsers.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(0.5)
        new_delivery_fee_text = self.browsers.find_element_by_xpath('//*[@id="root"]/div[2]/div[9]/div[4]/span[2]').text
        new_delivery_fee = float(new_delivery_fee_text[1:])
        if Package_delivery_fee != new_delivery_fee:
            print("商品登录前后，运费不一致")
            Package_delivery_fee = new_delivery_fee
        else:
            pass
        #这里需要调整
        if Package_total == Package_subtotal + Package_delivery_fee + Package_tax_fee - Package_coupons and Package_total == User_total:
            print('Order Confirmation 价格金额正确')
        else:
            print('Order Confirmation 价格金额异常')


deriver = Wed()
db_check = db_order_prodout.db_connector()
MysteryDetail_price = deriver.click_find_element(url='https://m-test.luckydeal.vip/main/product?productId=101506',element="//*[@id='root']/div[6]/div/a[2]/span[1]")
# Confirmation_price = deriver.check_Confirmation_element(url='https://m-test.luckydeal.vip/pay?productId=100000092&productType=1&qty=1')
# db_price = db_check.select_product_id_only_one_price(table='lucky_order_product',field='product_price',id=100000092)
# if MysteryDetail_price != Confirmation_price != db_price:
#     print("价格异常")
# else:
#     print("Confirmation_price、MysteryDetail_price 页面价格一致")

