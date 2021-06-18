import glob
import pandas as pd
from IPython.display import display


csv_from_zon_processed = glob.glob("csv_from_zon_processed\*_processed.csv")

csv_from_octoparse = glob.glob("csv_from_octoparse\*_seller.csv")

csv_from_octoparse_search = glob.glob("csv_from_octoparse_search\*")


df_zon_processed = pd.read_csv("csv_from_zon_processed\\Men Hoodies_processed.csv")
print(df_zon_processed.count())

df_octoparse = pd.read_csv("csv_from_octoparse\\Men Hoodies_octoparse_seller.csv")
print(df_octoparse.count())

#df_octoparse_search = pd.read_csv(csv_from_octoparse_search[0])

merge_df = df_zon_processed.merge(df_octoparse, 
                                  left_on="ASIN", 
                                  right_on="ASIN_from_page_url",
                                  how="left")



#merge_df = pd.merge(df_zon_processed, df_octoparse, how="left", on=["ASIN", "ASIN_from_page_url"])

print(merge_df.count())
merge_df.to_csv("merged.csv")

