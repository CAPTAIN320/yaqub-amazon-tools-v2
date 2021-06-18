from requests_html import HTMLSession

merchant_ID = "A2FJMYU3Q5P5P5"
url = "https://www.amazon.com/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&seller={}"
url2 = "https://www.amazon.com/sp?_encoding=UTF8&seller={}"

merchant_url = url.format(merchant_ID)
merchant_url2 = url2.format(merchant_ID)

print(merchant_url)
print(merchant_url2)

def getAddress(url):
    s = HTMLSession()
    r = s.get(url)
    print(r)
    #r.html.render(sleep=1)
    seller = {
        #'seller_name': r.html.xpath('//*[@id="storefront-link"]/a', first=True).text,
        #'address': r.html.xpath('//*[@id="seller-profile-container"]/div[2]/div/ul/li[2]', first=True).text
        "hello": "hello"
    }
    print(seller)
    return seller


getAddress('https://www.amazon.com/sp?_encoding=UTF8&asin=&isAmazonFulfilled=&isCBA=&marketplaceID=ATVPDKIKX0DER&orderID=&protocol=current&seller=A33GWWB6L3BHAV&sshmPath=')
