# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

if __name__ == "__main__":
    # TODO: write some Python code here to produce the desired output

    import os
    from dotenv import load_dotenv

    load_dotenv()

    tax_rate = float(os.getenv("TAX_RATE",default=.0875))

    # ASK FOR USER INPUT

    print("This program allows the user to input product indentifiers, searches for the corresponding products and prices, and prints a receipt.")
    print("You will begin by entering product identifiers. When you are done, enter 'DONE' when prompted for an input.")

    product_id = input("Please input a product identifier: ")

    clerk_inputs = []

    while product_id.upper() != "DONE":

        #validate user input
        #product IDs are valid between 1 and 20
        #if valid, add to list of inputs
        if int(product_id) > 0 and int(product_id) < 20:
    
            clerk_inputs.append(product_id)

        #not valid input
        else:

            print("Are you sure that product identifier is correct? Please try again!")

        product_id = input("Please input a product identifier: ")


    # LOOK UP CORRESPONDING PRODUCTS AND PRICES

    matching_products = []
    prices = []
    array_index = 0

    while array_index < len(clerk_inputs):
        for x in products:
            if str(x["id"]) == clerk_inputs[array_index]:
                #this is a match
                matching_products.append(x["name"])
                prices.append(x["price"])
        array_index = array_index + 1


    # print receipt

    # date and time
    # https://www.tutorialspoint.com/python/python_date_time.htm
    from time import ctime

    print("-----------------------------")
    print("One-Stop Shop Grocery")
    print("www.one-stop-shop.com")
    print("-----------------------------")
    print("CHECKOUT AT:", ctime())
    print("-----------------------------")

    #print selected products and corresponding price
    print("SELECTED PRODUCTS:")

    index = 0

    while index < len(matching_products):
        print("...", matching_products[index], "(" + to_usd(prices[index]) + ")")
        index = index + 1

    print("-----------------------------")

    #print subtotal
    index = 0

    subtotal = 0

    while index < len(prices):
        subtotal = prices[index] + subtotal
        index = index + 1

    print("SUBTOTAL:", to_usd(subtotal))

    #print tax

    tax = subtotal * tax_rate

    print("TAX:", to_usd(tax))

    #print total

    total = subtotal + tax

    print("TOTAL:", to_usd(total))

    print("-----------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
    print("-----------------------------")

    email_receipt = input("Would you like this receipt emailed to you? Please enter 'yes' or 'no: ")

    if email_receipt.lower() == "yes":
        import os
        from dotenv import load_dotenv
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        load_dotenv()

        SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
        SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))

        subject = "Your Receipt from the Green Grocery Store"
        html_content = "Your total is " + to_usd(total) + "." "The date is " + ctime() + "."
        print(html_content)

        # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
        # ... but we can customize the `to_emails` param to send to other addresses
        message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

        try:
            response = client.send(message)

            print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            print(response.status_code) #> 202 indicates SUCCESS
            print(response.body)
            print(response.headers)

        except Exception as err:
            print(type(err))
            print(err)
    
    else:
        print("Thank you! Have a great day.")
    