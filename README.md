# yaqub-amazon-tools-v2

##How it Works

csv files initially all go to csv_from_zon folder

zon_csv.py processes the files and saves them in csv_from_zon_processed folder

the files ("URL" column) are then fed into octoparse

octoparse scrapes seller info and saves its results to csv_from_octoparse

octoparse_csv.py then processes the files and saves them in csv_from_octoparse_processed folder

the files ("brand_url" column) are then fed into octoparse

octoparse scrapes and saves the no_of_search_results for each brand in csv_final_scrape

concantenate.py then concantenates files in the folders csv_from_zon_processed, csv_from_octoparse_processed, and csv_final_scrape  and then stores it in csv_concantenated

html.py then creates html files from csv_final and stores them in html



part 1 
1. get ASIN and/or Brand and/or URLs using ZonAsin
2. remove duplicate ASINs and/or brands
3. create brand_url for each brand (based on category)
4. export CSV to a different folder

part 2
1. scrape urls to get Brand, Seller Name, Seller URL and Seller Address using Octoparse
2. export CSV file
3. properly link each scraped url's data to the data in part 1 (use common identifier to concantenate the two tables, ASIN urls in this case)


part 4 
1. scrape no. of search_results from Amazon US brand url using Octoparse
2. concantenate the results into the above CSV file
3. export CSV file with only necessary headers

part 5
1. create html file for the final csv file


using ZONASIN
ASIN, ZonBrand, ZonUrl

using Octoparse
Page_URL, ASIN, Brand, Seller_Name, Seller_URL, Seller_ID, Seller_Address

using Python
concantente the two tables
