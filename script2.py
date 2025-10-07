"""https://insider-portal.atlassian.net/wiki/spaces/OPT/pages/3454468166/3.+Kal+t+m+devi"""

class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin  # boolean
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print(f"{self.push_type} Push gönderildi!")



class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type="Trigger")
        self.trigger_page = trigger_page



class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type="Bulk")
        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type="Segment")
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, price_info, discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type="PriceAlert")
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self, price_info, discount_rate):
        discounted_price = price_info * (1 - discount_rate)
        return discounted_price


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type="Instock")
        self.stock_info = stock_info

    def stockUpdate(self):
        self.stock_info = not self.stock_info
        return self.stock_info



trigger_push = TriggerPush("Web", True, 3, "2025-09-30", "2025-10-07", "TR", "home_page")
trigger_push.send_push()


bulk_push = BulkPush("Mobile", True, 5, "2025-09-30", "2025-10-10", "EN", 5)
bulk_push.send_push()

segment_push = SegmentPush("Web", False, 2, "2025-09-30", "2025-10-15", "TR", "premium_users")
segment_push.send_push()


price_alert_push = PriceAlertPush("Mobile", True, 4, "2025-09-30", "2025-10-05", "EN", 1000, 0.2)
discounted_price = price_alert_push.discountPrice(price_alert_push.price_info, price_alert_push.discount_rate)
print(f"Discounted Price: {discounted_price}")
price_alert_push.send_push()

instock_push = InstockPush("Web", True, 3, "2025-09-30", "2025-10-08", "TR", True)
print(f"Stock before update: {instock_push.stock_info}")
updated_stock = instock_push.stockUpdate()
print(f"Stock after update: {updated_stock}")
instock_push.send_push()




trigger_push = TriggerPush("Web", True, 3, "2025-09-30", "2025-10-07", "TR", "home_page")
trigger_push.send_push()


bulk_push = BulkPush("Mobile", True, 5, "2025-09-30", "2025-10-10", "EN", 5)
bulk_push.send_push()


segment_push = SegmentPush("Web", False, 2, "2025-09-30", "2025-10-15", "TR", "premium_users")
segment_push.send_push()

price_alert_push = PriceAlertPush("Mobile", True, 4, "2025-09-30", "2025-10-05", "EN", 1000, 0.2)
discounted_price = price_alert_push.discountPrice(price_alert_push.price_info, price_alert_push.discount_rate)
print(f"Discounted Price: {discounted_price}")
price_alert_push.send_push()


instock_push = InstockPush("Web", True, 3, "2025-09-30", "2025-10-08", "TR", True)
print(f"Stock before update: {instock_push.stock_info}")
updated_stock = instock_push.stockUpdate()
print(f"Stock after update: {updated_stock}")
instock_push.send_push()