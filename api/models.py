class News:

    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des
        self.img = img

news1 = News(
    "iPhone 16 Pro Max", 
    "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.", 
    "https://github.com/bakueduaz/images/blob/main/iphone_16_pro_max.png?raw=true"
)

news2 = News(
    "AirPods Pro 3", 
    "The AirPods Pro 3 are expected to feature new adaptive audio technology", 
    "https://github.com/bakueduaz/images/blob/main/Apple-AirPods-Pro-3.jpg?raw=true"
)

news3 = News(
    "Apple Watch Ultra 3",
    "The Apple Watch Ultra 3 will likely maintain the same rugged design as its", 
    "https://github.com/bakueduaz/images/blob/main/Apple-Watch-Ultra-3.jpg?raw=true"
)


news_list = [news1, news2, news3]