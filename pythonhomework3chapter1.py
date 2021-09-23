class WebPush:

    def __init__(self, Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):

        self.Platform = Platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push():
        print("‘Push gönderildi!’")

class TriggerPush(WebPush):

    trigger_page = "Homepage"
    WebPush.send_push()

class BulkPush(WebPush):

    send_date = int(51)
    WebPush.send_push()

class SegmentPush(WebPush):

    segment_name = str("Book Searchers")
    WebPush.send_push()

class PriceAlertPush(WebPush):

    def discountPrice(price_info, discount_rate):

        price_info = price_info
        discount_rate = discount_rate
        WebPush.send_push()

        return price_info, discount_rate

class InstockPush(WebPush):

    def stockUpdate(stock_info):

        if(stock_info == True):

            stock_info = False

        else:
            stock_info = True

        WebPush.send_push()
        return stock_info

WebPush_ = WebPush("Chrome", True, "Three_views_in_24hours", "09.19.2021", "10.19.2021", "ENG", "Pop_Up")

PriceInfo_ = int(input("Please enter Price Info:"))
DiscountRate_ = float(input("Please enter Discount Rate:"))
stock_info = bool(input("Please enter Stock Info Update:"))

AbouttheDiscount = PriceAlertPush.discountPrice(PriceInfo_, DiscountRate_)
print(AbouttheDiscount)

TriggerPush.send_push()

BulkPush.send_push()

SegmentPush.send_push()

WebPush.send_push()





