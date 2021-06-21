# declare dictionary of foods

# STEP 2
food_prices = {"Chicken":1.59, 
               "Beef":1.99, 
               "Cheese":1, 
               "Milk":2.50}

# STEP 3
artist_genre = {"Romeo Santos": "Bachata",
                "Jill Scott": "RnB",
                "The Pharcyde": "Hip Hop",
                "Al Green": "Soul"}

#EXAMPLE
print(artist_genre["Romeo Santos"])

# STEP 4
chicken = food_prices["Chicken"]
beef = food_prices["Beef"]
cheese = food_prices["Cheese"]
milk = food_prices["Milk"]

print("The price of chicken is", chicken)
print("The price of beef is", beef)
print("The price of cheese is", cheese)
print("The price of milk is", milk)

# STEP 5

food_prices["Chicken"] = 3


# STEP 6
shoe_inv = {"Jordan 13":1,
            "Yeezy":8,
            "Foamposite":10,
            "Air Max":5,
            "SB Dunk":20}

   # LAB 4 
# EXAMPLE
def triangle_area( base, height):

    area = 1/2 * base * height
    return area

print(triangle_area(3, 4))

def total_price(food_1, food_2):

    total = food_prices[food_1] + food_prices[food_2]
    
    return total

print(total_price("Beef", "Cheese"))

def price_diff(food_1, food_2):

    total = food_prices[food_1] - food_prices[food_2]
    
    if total < 0:
        
        return "Price cannot be less than 0."
    
    else:
        
        return total

print(price_diff("Beef", "Cheese"))

# STEP 4
shoe_inv = {"Jordan 13": 1, "Yeezy": 1, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

def restock(shoe_name, multiplier):
    newInv = shoe_inv[shoe_name] * multiplier
    shoe_inv[shoe_name] = newInv
    return shoe_inv


def clearance_sale(shoe_name, discount):
    salePrice = shoe_inv[shoe_name] / discount
    shoe_inv[shoe_name] = salePrice
    return shoe_inv
