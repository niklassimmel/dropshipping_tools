# tool gibt aus was die beste wahl ist an supplier (price, shipping, time)
# simple version basierend auf input numbers und komplexe version mit webscraping basierend auf reviews von store, order nrs, etc.

# simple version
# input listingprice
# calculate steuer drauf
# input shippingprice
# input where it ships from
# input shippingdauer (experience)
# 


listing_link = input("Please provide the link of the listing: ") #str
listing_price = (input("What's the listing price: ") #float

if type(listing_price) == str:
    listing_price = listing_price.replace(",", ".") #replaces , mit .
elif type(listing_price) == int:
    listing_price = float(listing_price)


shipping_country = input("Where does the item ship from: ") #str
shipping_price = float(input("What's the shippingprice: ")) #float
shipping_time = input("How long is the max shipping time: ") #int

def calculateNumbers():
    #tax
    tax = listing_price * 0.2
    tax_price = listing_price + tax

    # shipping
    new_price = tax_price + shipping_price

    # statement

    print(f"The item from this supplier costs you a total of {new_price} including listing price at {listing_price}, tax at {tax}, and shipping price at {shipping_price}!")
    print(f"The item ships from the {shipping_country} and takes a max of {shipping_time} days!")

calculateNumbers()


#errors drinnen aber keien zeit mehr
# fuck yeah code is fucking fun -- i will code a fucking lot once the store is up and running we're going to kill it fuck yeah