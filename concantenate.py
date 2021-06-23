import glob
import re
import pandas as pd
from IPython.display import display


csv_from_zon_processed = glob.glob("csv_from_zon_processed\*_processed.csv")

csv_merchant_octo = glob.glob("csv_merchant_octo\*_merchant_octo.csv")

csv_product_octo = glob.glob("csv_product_octo\*_product_octo.csv")


df_zon_processed = pd.read_csv("csv_from_zon_processed\\Women Jewelry_processed.csv")
print(df_zon_processed.count())

df_merchant_octo = pd.read_csv("csv_merchant_octo\\Women Jewelry_merchant_octo.csv")
print(df_merchant_octo.count())

df_product_octo = pd.read_csv("csv_product_octo\\Women Jewelry_product_octo.csv")

""" Better way of finding merchant_ID using regex
string = "https://www.amazon.com/sp?_encoding=UTF8&asin=&isAmazonFulfilled=1&isCBA=&marketplaceID=ATVPDKIKX0DER&orderID=&protocol=current&seller=A12AWXEV5DO25C&sshmPath="
pattern = "&seller=.*&"
result = re.findall(pattern, string)
result = result[0][8:-1]
print(result)
 """

def csv_merchant_octo():
    print("hello")
    merchant_id_octo = []
    for url in df_merchant_octo["Page_URL"]:
        merchant_id_from_url = url[135:-10]
        merchant_id_octo.append(merchant_id_from_url)
        
    df_merchant_octo["merchant_id_octo"] = merchant_id_octo
    print(df_merchant_octo["merchant_id_octo"])

    df_merchant_octo["business_address"] = df_merchant_octo["business_address"].astype(str)
    country_merchant_octo = []
    for merchant_address in df_merchant_octo["business_address"]:
        country_merchant = merchant_address[-2:]
        country_merchant_octo.append(country_merchant)

    df_merchant_octo["country_merchant_octo"] = country_merchant_octo

    merge_df = df_zon_processed.merge(df_merchant_octo, 
                                    left_on="MerchantID", 
                                    right_on="merchant_id_octo",
                                    how="left")
    
    return merge_df

    
    


def csv_product_octo():
    df_product_octo["seller_address"] = df_product_octo["seller_address"].astype(str)
    country_product_octo = []
    for product_address in df_product_octo["seller_address"]:
        country_product = product_address[-2:]
        country_product_octo.append(country_product)

    df_product_octo["country_product_octo"] = country_product_octo


    merge_df = csv_merchant_octo().merge(df_product_octo,
                                    left_on="ASIN",
                                    right_on="ASIN_from_page_url",
                                    how="left")

    print(merge_df.count())
    return merge_df


def merge_csv(merge_df):# (ouptut_of_merchant, output_of_product)
    print()
    

def export_csv(merge_df):
    merge_df.to_csv("concantenated\\2nd_merged.csv")
    
def export_html(merge_df):
    merge_df = merge_df[["Brand", 
                         "SoldBy", 
                         "MerchantID", 
                         "US_brand_link", 
                         "JP_brand_link", 
                         "country_merchant_octo",
                         "country_product_octo"]]
    merge_df.to_html("html\\2nd_merged.html", escape=False)



csv_merchant_octo()
merge_df = csv_product_octo()
export_csv(merge_df)
export_html(merge_df)


