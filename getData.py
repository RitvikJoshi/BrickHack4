from BrickHack4 import getLocationData
from BrickHack4.getProductData import getProductData


def main():
    productDetails = getProductData("sugar")

    for i in range(len(productDetails)):
        print('Results ::', i, productDetails[i])
        ItemNumber = productDetails[i]['ItemNumber']
        locationDetails = getLocationData(ItemNumber)
        print('\tLocation ::')




main()
