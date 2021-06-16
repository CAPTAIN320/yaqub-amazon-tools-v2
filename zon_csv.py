import glob
import pandas as pd
import logging

# a dictionary of Amazon categories with their corresponding Top-Level category
top_level_categories_dict = {
                        "Appliances": "Appliances",
                        "Beauty & Personal Care": "Beauty & Personal Care",
                        "Clothing, Shoes & Jewelry": "Clothing, Shoes & Jewelry",
                        "Electronics": "Electronics",
                        "Handmade": "Handmade",
                        "Sports & Outdoors": "Sports & Outdoors",
                        "Tools & Home Improvement": "Tools & Home Improvement",
                        "Toys & Games": "Toys & Games",
                        "Office Products": "Office Products",
                        "Women Bags & Wallets": "Clothing, Shoes & Jewelry",
                        "Women Jewelry": "Clothing, Shoes & Jewelry",
                        "Men Jewelry": "Clothing, Shoes & Jewelry",
                        "Girl Jewelry": "Clothing, Shoes & Jewelry",
                        "Boy Jewelry": "Clothing, Shoes & Jewelry",
                        "Power Tools": "Tools & Home Improvement",
                        "Boy Hoodies": "Clothing, Shoes & Jewelry",
                        "Men Hoodies": "Clothing, Shoes & Jewelry",
                        "Men Jackets": "Clothing, Shoes & Jewelry",
                        "Women Hoodies": "Clothing, Shoes & Jewelry",
                        "Girl Hoodies": "Clothing, Shoes & Jewelry",
                        "Men Watches": "Clothing, Shoes & Jewelry",
                        "Men Bags": "Clothing, Shoes & Jewelry",
                        "Men Wallets": "Clothing, Shoes & Jewelry",
                        "Women Watches": "Clothing, Shoes & Jewelry",
                        "Women Wallets": "Clothing, Shoes & Jewelry",
                        "Card Games": "Toys & Games",
                        "Board Games": "Toys & Games",
                        "Women Pumps (shoes)": "Clothing, Shoes & Jewelry",
                        "Women Flats (shoes)": "Clothing, Shoes & Jewelry",
                        "Women Boots (shoes)": "Clothing, Shoes & Jewelry",
                        "Women Loafers (shoes)": "Clothing, Shoes & Jewelry",
                        "Jewelry Accessories": "Clothing, Shoes & Jewelry",
                        "Puzzles": "Toys & Games",
                        "Building Toys": "Toys & Games",
                        "Sports & Outdoor Play": "Toys & Games",
                        "Necklaces & Pendants": "Clothing, Shoes & Jewelry",
                        "Stuffed Animals & Plush Toys": "Toys & Games"
                        }

# a dictionary of Amazon categories with their corresponding Amazon ID
categories_ID_dict = {
                        # "Category": [US_category_ID, JP_category_ID] 0 = no ID
                        "Appliances": [2619525011, 124048011],
                        "Beauty & Personal Care": [3760911, 52374051],
                        "Clothing, Shoes & Jewelry": [7141123011, 352484011],
                        "Electronics": [172282, 3210981],
                        "Handmade": [11260432011, 0],
                        "Sports & Outdoors": [3375251, 14304371],
                        "Tools & Home Improvement": [228013, 2016929051],
                        "Toys & Games": [165793011, 13299531],
                        "Musical Instruments": [11091801, 2123629051],
                        "Office Products": [1064954, 86731051],
                        "Women Bags & Wallets": [15743631, 2221075051],
                        "Women Jewelry": [7192394011, 5519723051],
                        "Men Jewelry": [3887881, 86246051],
                        "Girl Jewelry": [3880961, 0],
                        "Boy Jewelry": [3880611, 0],
                        "Power Tools": [551236, 0],
                        "Boy Hoodies": [5604815011, 2131573051],
                        "Men Hoodies": [1258644011, 2131434051],
                        "Men Jackets": [1045830, 2131419051],
                        "Women Hoodies": [1258603011, 2131504051],
                        "Girl Hoodies": [5604818011, 2131598051],
                        "Men Watches": [6358539011, 333009011],
                        "Men Bags": [14864589011, 5355946051],
                        "Men Wallets": [7072333011, 2221209051],
                        "Women Watches": [6358543011, 333010011],
                        "Women Wallets": [7072326011, 2221186051],
                        "Card Games": [166239011, 2189604051],
                        "Board Games": [166225011, 2189603051],
                        "Women Pumps (shoes)": [679416011, 2221092051],
                        "Women Flats (shoes)": [679399011, 2221083051],
                        "Women Boots (shoes)": [679380011, 2221085051],
                        "Women Loafers (shoes)": [679404011, 2221090051],
                        "Jewelry Accessories": [9616098011, 86252051],
                        "Puzzles": [166359011, 2189596051],
                        "Building Toys": [166092011, 2189163051],
                        "Sports & Outdoor Play": [166420011, 2189318051],
                        "Women Necklaces & Pendants": [7454934011, 86228051],
                        "Stuffed Animals & Plush Toys": [166461011, 2189188051]
                        }

#read file names
csv_from_zon = glob.glob("csv_from_zon\*.csv")

#array of csv files
csv_from_zon_array = []
#loop to create array of csv files
for file in csv_from_zon:
    csv_from_zon_array.append(file)

#loops through each csv file in the array
for current_file in csv_from_zon_array:

    print("Now Processing: "+ current_file[13:].title())

    current_file_name = current_file[13:-4]

    #gets category ID of respective Amazon stores
    selected_US_category = categories_ID_dict[current_file_name][0]
    selected_JP_category = categories_ID_dict[current_file_name][1]

    #reads csv file and assigns it to a dataframe
    df = pd.read_csv(current_file, 
                    dtype={"ASIN": "string", "Brand": "string", "Category": "string", "SalesRank": int})
    
    #removes duplicate ASIN
    df = df.drop_duplicates(subset=["ASIN"])
    
    #sets ASIN as the index (unique ID) of the dataframe
    df = df.set_index("ASIN", drop=False)
    
    #retains only ASINs with a Brand
    df = df[df["Brand"].notnull()]

    #removes duplicate Brand
    df = df.drop_duplicates(subset=["Brand"])

    #array of brand_url of respective Amazon stores
    us_brand_url_array = []
    jp_brand_url_array = []
    #loop to create urls using Brand column for respective Amazon store
    for key, value in df["Brand"].iteritems():
        #replace blank spce with a "+" for each brand name
        value = value.replace(" ", "+")
        #create the urls
        us_search_url = "https://www.amazon.com/s?rh=n%3A{}%2Cp_89%3A{}"
        jp_search_url = "https://www.amazon.co.jp/s?rh=n%3A{}%2Cp_89%3A{}"
        #concantenate category ID and Brand names into url
        us_brand_url = us_search_url.format(selected_US_category,value)
        jp_brand_url = jp_search_url.format(selected_JP_category,value)
        #append brand urls
        us_brand_url_array.append(us_brand_url)
        jp_brand_url_array.append(jp_brand_url)
    
    #create column for Brand URLs
    df["US_brand_url"] = us_brand_url_array
    df["JP_brand_url"] = jp_brand_url_array

    #create column for the clickable links
    df["US_brand_link"] = '<a target="_blank" href=' + df["US_brand_url"] + '><div>' + df["Brand"] + '</div></a>'
    df["JP_brand_link"] = '<a target="_blank" href=' + df["JP_brand_url"] + '><div>' + df["Brand"] + '</div></a>'
    
    #generate and export csv file
    df.to_csv("csv_from_zon_processed\\"+current_file_name+".csv")
    

print("Finished")