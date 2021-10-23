import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import db
oyo_url="https://www.oyorooms.com/hotels-in-kolkata/?page="
parser=argparse.ArgumentParser()
parser.add_argument("--page_no_max",help="Enter number of pages to be parsed",type=int)
parser.add_argument("--dbname",help="Enter the database name",type=str)
args=parser.parse_args()

db.connect(args.dbname)
page_no_max=args.page_no_max
scraped_list=[]
for pageno in range(1,page_no_max):
    headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    url=oyo_url+str(pageno)
    print("Get request for->"+url)
    req=requests.get(oyo_url+str(pageno),headers=headers)
    content=req.content
    soup=BeautifulSoup(content,"html.parser")
    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
    for hotels in all_hotels:
        hotel={}
        hotel['name']=hotels.find("h3",{"class":"listingHotelDescription__hotelName"}).text
        hotel['address']=hotels.find("span",{"itemprop":"streetAddress"}).text
        hotel['price']=hotels.find("span",{"class":"listingPrice__finalPrice"}).text
        try:
            hotel['rating']=hotels.find("span",{"class":"hotelRating__rating"}).text
            hotel['ratingsummary']=hotels.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel['rating']=None
            hotel['ratingsummary']=None
        parent_amenities=hotels.find("div",{"class":"amenityWrapper"})
        hotel_amenities=[]
        for amenities in parent_amenities.find_all("div",{"class":"amenityWrapper__amenity"}):
            hotel_amenities.append(amenities.find("span",{"class":"d-body-sm"}).text.strip())
        hotel['amenities']=','.join(hotel_amenities[:-1])
        scraped_list.append(hotel)
        db.insert_into_table(args.dbname,tuple(hotel.values()))
df=pandas.DataFrame(scraped_list)
print("Creating csv file......")
df.to_csv("oyo_details.csv")
db.get_hotel_info(args.dbname)
