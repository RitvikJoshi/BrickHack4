
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('recipe_ingredient')
from getData import getData


def getRecipe(session):
    print(session)
    response = table.scan(
    ProjectionExpression="recipe_name",
    #FilterExpression=Attr('Country').eq(session)
    FilterExpression=Attr('Type').eq(session)
    )
    recipe_List =""
    for recipes in response['Items']:
     print(recipes['recipe_name'])
     recipe_List+=" "+recipes['recipe_name']+", "
    return recipe_List
    
    
def getIngrident(name):    
    ItemList =[]
    response = table.query(
    KeyConditionExpression=Key('recipe_name').eq(name)
    )
    
    for items in response['Items']:
       for key in items:
        if( 'Ingredient' in key):
         ItemList.append(items[key])
    
    
    cartList = getData(ItemList)  
    
    result=""
    missed=" ingredients that are not available are "
    miss_product=""
    for product in cartList:
      if(cartList[product].ItemNumber == 0):
       miss_product += product+", "
      else: 
       result+= cartList[product].Description+" of brand "+ cartList[product].Brand+ " and price $"+ str(cartList[product].Price)+", "
    
    #item = response['Item']
    if(miss_product==""):
     missed=""
    else:
     missed+=miss_product
     
    return result+missed
