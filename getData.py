from BrickHack4.getPriceData import getPriceData
from BrickHack4.getProductData import getProductData


def main():
    productDetails = getProductData("Oil")
    minPrice = 999999
    minStore = 0
    itemNo =0
    Brand =""
    Description=""
    limit1= 0
    limit2 = 0
    if(len(productDetails)>10):
        limit1= 10
    else:
        limit1 = len(productDetails)
    for i in range(limit1):
        #print('Results ::', i, productDetails[i])
        ItemNumber = productDetails[i]['ItemNumber']
        priceDetails = getPriceData(ItemNumber)
        #print('\tprice ::', priceDetails)
        if (len(priceDetails) > 10):
            limit2 = 10
        else:
            limit2 = len(priceDetails)

        for j in range(limit2):
            #print(store['Price'])
            store = priceDetails[j]
            if("Price" in store and store["Price"]<minPrice):
                minPrice=store["Price"]
                minStore = store["StoreNumber"]
                itemNo =ItemNumber
                Brand = productDetails[i]['Brand']
                Description = productDetails[i]['Description']
            else:
                pass
    print("ItemNumber :",itemNo," Brand :",Brand,"Descritpion :",Description,"price :",minPrice,'storeNum :',minStore)






main()
