import csv # used for loading the contents of csv file into the dictionary in loadStockFromFile() function


def loadStockFromFile(filename):
    """
    This fuction takes a string as a input which is used as the name of the file to read the csv file and return its content as a dictionary
    """
    try:
        f = open(filename , 'r')
        stock = {}
        items = csv.reader(f , delimiter='|')
        skipped = 0
        for i in items:
            try:
                stock[i[0]] = {'name':i[1], 'price':float(i[2]), 'unit':i[3], 'promotion':i[4], 'group':i[5], 'amount':i[6]}
                if stock[i[0]]['unit'] == 'pieces':
                    stock[i[0]]['amount'] = int(stock[i[0]]['amount'])
                else:
                    stock[i[0]]['amount'] = float(stock[i[0]]['amount'])
                if stock[i[0]]['promotion'] == 'None':
                    stock[i[0]]['promotion'] = None
                if stock[i[0]]['group'] == 'None':
                    stock[i[0]]['group'] = None
                else:
                    stock[i[0]]['group'] = int(stock[i[0]]['group'])

            except:
                stock[i[0]] = {'skipped': 'The Format is incorrect , Please Check '}
                skipped += 1
        return stock
    except IOError:
        print ("Could not read file:", filename)


def listItems(dct):
    """
    This fuction takes a dictionary as a perimeter and reads the dictionary and returns a string which is in tabular form
    """
    display = ""
    skipped = 0
    print("Ident | Product                              |   Price  |   Amount    \n" + "-"*70)
    for i in range(len(dct)):


        try:
            nameLen = len(dct[str(list(dct)[i])]['name'])
            priceLen = len(str(format(dct[str(list(dct)[i])]['price'])))
            if priceLen == 4 and dct[(list(dct)[i])]['price'] < 10:
                 priceLen = 3

            display += str(list(dct)[i] + ' |  '+ dct[str(list(dct)[i])]['name'] +' '*(35-nameLen) + ' | ' + ' '*(6 - priceLen) + format(dct[str(list(dct)[i])]['price'], '.2f')+ '£ ' + '|  '  + str(dct[str(list(dct)[i])]['amount']) + ' ' +str(dct[str(list(dct)[i])]['unit']) + '\n')
        except:
            skipped +=1

    return display


def searchStock(stock , str):
    """

    This fuction takes list(e.g stock in this case') and a string as a perimeter and search entered string from the given dictionary and returns a sub dictionary containing elements of that dictionary if found
    """
    skipped = 0
    subStock = {}

    for i in range(len(stock)):
        try:
            if str.title() in stock[(list(stock)[i])]['name']:
                subStock[list(stock)[i]] = {'name':stock[(list(stock)[i])]['name'], 'price': stock[(list(stock)[i])]['price'], 'unit':stock[(list(stock)[i])]['unit'], 'promotion':stock[(list(stock)[i])]['promotion'], 'group':stock[(list(stock)[i])]['group'], 'amount': stock[(list(stock)[i])]['amount']}
        except:
            skipped += 1



    return subStock


def addToBasket(stock, basket, ident, amount):
    """

    This fuction takes two list(e.g stock and basket in this case'), a string and a float as a perimeter add and remove amount from stock dictionary to basket and vice versa based on the string and float. This does not return anything since the dictionaries are being updated automatically
    """
    try:
        if not bool(basket):
            basket[ident] = {'name':stock[ident]['name'], 'price': stock[ident]['price'], 'unit':stock[ident]['unit'], 'promotion':stock[ident]['promotion'], 'group':stock[ident]['group'], 'amount': 0 }

        else:
            if  ident in basket:
                None
            else:
                basket[ident] = {'name':stock[ident]['name'], 'price': stock[ident]['price'], 'unit':stock[ident]['unit'], 'promotion':stock[ident]['promotion'], 'group':stock[ident]['group'], 'amount': 0 }


        if amount == 0:
            return None

        elif amount>0 and amount<=stock[ident]['amount']:
            basket[ident]['amount'] = basket[ident]['amount'] + amount
            stock[ident]['amount'] = stock[ident]['amount'] - amount
            return None

        elif amount>0 and amount>stock[ident]['amount']:
            basket[ident]['amount'] = basket[ident]['amount'] + stock[ident]['amount']
            n = stock[ident]['amount']
            stock[ident]['amount'] = 0.0
            return ('Cannot add this many '+ stock[ident]['unit'] + ' to the basket, only added '+ str(n) + ' ' + str(stock[ident]['unit']))

        elif amount<0 and (-amount)<= basket[ident]['amount']:
            stock[ident]['amount'] = stock[ident]['amount'] + (-amount)
            basket[ident]['amount'] = basket[ident]['amount'] + amount
            if basket[ident]['amount'] == 0:
                del basket[ident]
            return None

        elif amount<0 and (-amount) > basket[ident]['amount']:
            stock[ident]['amount'] = stock[ident]['amount'] + basket[ident]['amount']
            n = basket[ident]['amount']
            del basket[ident]
            return ('Cannot add this many '+ stock[ident]['unit'] + ' from the basket, only added '+ str(n) + ' ' + str(stock[ident]['unit']))

    except:
        return 'please double check your values'


def prepareCheckout(basket):
    """

    This fuction takes list(e.g basket in this case') as a perimeter and adds an extra key amountPayable to the dictionary with the same value of amount from that dictionary
    """
    for i in range(len(basket)):
          basket[list(basket)[i]]["amountPayable"] =  basket[list(basket)[i]]['amount']


def applyPromotions(basket):
    """

    This fuction takes list(e.g basket in this case') as a perimeter and calculates the discount on the promotion and update actualyPayable depending on promotions
    """
    for i in range(len(basket)):
        if basket[list(basket)[i]]['promotion'] == 'get2pay1':
            basket[list(basket)[i]]['amountPayable'] = basket[list(basket)[i]]['amountPayable'] - int(basket[list(basket)[i]]['amountPayable']/2)
        elif basket[list(basket)[i]]['promotion'] == 'get4pay3':
            basket[list(basket)[i]]['amountPayable'] = basket[list(basket)[i]]['amountPayable'] - int(basket[list(basket)[i]]['amountPayable']/4)
        else:
             None



def getBill(basket):
    """

    This fuction takes a list (e.g basket in this case') and generates a bill and returns it as nice formatted string in a tabular form. This function also calculate the TOTAL amount that needs to be paid after applying all the discounts
    """

    applyPromotions(basket)
    print("Product                             |   Price   |  Amount     |  Payable  \n" + "-"*73)
    total = 0.0
    display = ""
    for i in range(len(basket)):
        nameLen = len(basket[str(list(basket)[i])]['name'])
        priceLen = len(str(format(basket[str(list(basket)[i])]['price'])))
        amountPayable = str(format(float(basket[str(list(basket)[i])]['amount']) * float(basket[str(list(basket)[i])]['price']), '.2f'))
        discountedAmount = basket[(list(basket)[i])]['amount'] - basket[(list(basket)[i])]['amountPayable']
        discountedPayable = str(format(float(discountedAmount) * float(basket[str(list(basket)[i])]['price']), '.2f'))
        unitLen = len(basket[str(list(basket)[i])]['unit'] + str(format(basket[str(list(basket)[i])]['amount'])))
        discountedlen = len(str(discountedAmount)+basket[str(list(basket)[i])]['unit'])
        total += float(amountPayable) - float(discountedPayable)
        if basket[str(list(basket)[i])]['promotion'] == None:
            basket[str(list(basket)[i])]['promotion'] = str(None)+"    "
        if priceLen == 4 and basket[(list(basket)[i])]['price'] < 10:
             priceLen = 3

        display +=  basket[str(list(basket)[i])]['name'] +' '*(35-nameLen) + ' | ' +  ' '*(6 - priceLen) + format(basket[str(list(basket)[i])]['price'], '.2f') +  ' £' + ' |  '  +  str(basket[str(list(basket)[i])]['amount'])+ ' ' +str(basket[str(list(basket)[i])]['unit']) + " "*(10-unitLen)+ " |   "+ amountPayable+ ' £' + '\n' + "    Promotion "+ basket[str(list(basket)[i])]['promotion'] + '              |' +  ' '*(6 - priceLen) + "-"+format(basket[str(list(basket)[i])]['price'], '.2f')+ ' £' + ' |  ' + str(discountedAmount)+' ' +str(basket[str(list(basket)[i])]['unit']) + " "*(9-discountedlen) + '  |  ' +'-'+ discountedPayable +' £'+ "\n"

    display += '-'*73+'\nTOTAL:'+ (' '*60) + str(total) + ' £'
    return display


def main():
    """
    This is the main fuction to mimic a self-checkout system which allows the customer to list the products on stock, add (remove) products from the stock to their shopping basket, list the items in the basket, and display a bill for the basket.
    """
    stock = loadStockFromFile('stock.csv')
    basket = {}
    print("*"*75)
    print("*"*15+" "*10+"WELCOME TO SUPERMARKET"+" "*10+"*"*15)
    print("*"*75,"\n")
    while True:
        s = input("Input product-Ident, search string, 0 to display basket, 1 to check out: ")
        if s == "0":
            if not bool(basket): # checks if the basket is empty
                    print("Your Baket is empty")
            else:
                print("Your current shopping basket: \n")
                displayBasket = listItems(basket)
                print(displayBasket)

        elif s == "1":
            print("Your Bill is :\n")
            prepareCheckout(basket)
            bill = getBill(basket)
            print(bill)
            print('\nThank you for shopping with us!')
            break

        elif s in stock:

            try: # for handling exceptions for the enteries which have been skipped
                if stock[s]["skipped"] == "The Format is incorrect , Please Check " :
                    print("This value has been skipped , please double check the value and re-enter in stock")
            except:
                while True:
                    try: # for handling exceptions such as user entering wrong format
                        nr = float(input("How many " + stock[s]['unit'] + " do you want to add to your basket? : "))
                        break
                    except:
                        print("Error! Please Enter the correct Input")

                msg = addToBasket(stock, basket, s, nr)
                if msg != None:
                    print(msg)
        else:
            substock = searchStock(stock, s)
            print("There were " +str(len(substock)) + " search results for '" + str(s) +"': \n")
            if len(substock) == 0:
                None
            else:
                displaySubstock = listItems(substock)
                print(displaySubstock)

        print("\n")

if __name__ == '__main__':
    main()
