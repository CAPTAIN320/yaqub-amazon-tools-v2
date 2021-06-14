# yaqub-amazon-tools-v2

##How it Works

csv files initially all go to csv_from_zon folder

zon_csv.py processes the files and saves them in csv_from_zon_processed folder

the files (urls column) are then fed into octoparse

octoparse scrapes and saves its results to csv_from_octoparse

octoparse_csv.py then processes the files and saves them in csv_from_octoparse_processed folder

url_creator.py then processes the files and saves them in csv_from_url_creator

the files (brand_urls column) are then fed into octoparse

octoparse scrapes and saves the no_of_search_results for each brand in csv_from_octoparse_no_2

final.py then concantenates the results with the files in csv_from_url_creator and then stores it in csv_final

html.py then creates html files from csv_final and stores them in html