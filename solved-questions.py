""" 1. sum of integers up to single decimal"""

def summ(num):
	sum_of_integers = 0
	while(num):
		sum_of_integers += num%10
		num = num//10
		if num == 0 and len(str(sum_of_integers)) > 1:
			num = sum_of_integers
			sum_of_integers = 0
	return sum_of_integers

""" 2. list of occurences of values """

liste = [1,2,3,4,5,6,4,6,8]

opt = {}
for i in liste:
	if i in opt.keys():
		opt[i]=opt[i]+1 
	else:
		opt[i]=1
print(opt)

""" 3. find the number of occurences of substr in the string """

def secretInfo(text, name):
	# Write your code here
	return text.count(name)

def main():
	#input for text
	text = str(input())
	
	#input for name
	name = str(input())
	
	
	result = secretInfo(text, name)
	print(result)	

if __name__ == "__main__":
	main()


""" 4. find the number of common products used the customers.
3 4 ---- 3 is num of customers and 4 is the number of products bought by them.
1 2 4 5
4 6 2 3
4 6 7 8

output 4
"""

# tag, representing the matrix of 'tag_row * tag_col' size, 
# where tag_row & tag_col are number of customers and number of products.
def sortedProduct(tag):
    # Write your code here
    products = None
    for row in tag:
        if products is None:
            products = set(row)
        else:
            products = products.intersection(set(row))
    products = list(products)
    products.sort()
    return products

def main():
    #input for tag
    tag = []
    tag_rows,tag_cols  = map(int, input().split())

    for idx in range(tag_rows):
        tag.append(list(map(int, input().split())))
    
    result = sortedProduct(tag)
    print(" ".join([str(res) for res in result]))   

if __name__ == "__main__":
    main()

""" 5. find the total price of orders and only apply the discount to highest price in order, rest sum the prices

input:

20
3
100 400 200

output:
620 """


import sys
import math
from contextlib import redirect_stdout


def calculate_total_price(prices, discount):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    net_amt = 0
    prices.sort()
    highest_amount = prices[-1]
    total_price = 0
    if discount:
        discount_amount = (highest_amount*discount)/100
        net_amt = highest_amount - discount_amount
    for i in range(0, len(prices)-1 if discount else len(prices)):
        total_price += prices[i]
    return math.floor(net_amt+total_price)

# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    discount = int(input())
    n = int(input())
    prices = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        price = calculate_total_price(prices, discount)
    print(price)


if __name__ == "__main__":
    main()


""" 6. find which player has scored the points win or lost 

score = 0
score1 = 15
score2 = 30
score3 = 40

input:
rahul
fren
3
rahul
rahul
rahul

output:
rahul 40 - fren 0 """

import sys
import math
from contextlib import redirect_stdout


def compute_game_state(name_p1, name_p2, wins):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    score = 0
    score1 = 15
    score2 = 30
    score3 = 40
    opt = {}
    x = ''
    y = ''
    for i in wins:
        if i in opt.keys():
            opt[i]=opt[i]+1
        else:
            opt[i]=1

    if opt.get(name_p1) is None:
        x = f"{name_p1} {score}"
    if opt.get(name_p1) == 1:
        x =  f"{name_p1} {score1}"
    elif opt.get(name_p1) == 2:
        x = f"{name_p1} {score1}"
    elif opt.get(name_p1) == 3:
        x =  f"{name_p1} {score3}"
    elif opt.get(name_p1) == 4:
        return "{name_p1} WINS"


    if opt.get(name_p2) is None:
        y = f"{name_p2} {score}"
    if opt.get(name_p2) == 1:
        y = f"{name_p2} {score1}"
    elif opt.get(name_p2) == 2:
        y = f"{name_p2} {score2}"
    elif opt.get(name_p2) == 3:
        y = f"{name_p2} {score3}"
    elif opt.get(name_p2) == 4:
        return "{name_p2} WINS"

    if opt.get(name_p1) is None and opt.get(name_p2) is None:
    	return " - "
    return f"{x} - {y}"

# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    name_p1 = input()
    name_p2 = input()
    played_count = int(input())
    wins = []
    for i in range(played_count):
        wins.append(input())
    with redirect_stdout(sys.stderr):
        game_state = compute_game_state(name_p1, name_p2, wins)
    print(game_state)


if __name__ == "__main__":
    main()

""" 7. decorator in python that will count how many times the decorated function was called """

def get_func_count(func):
    def func_count(x):
        func_count.calls += 1
        return func(x)
    func_count.calls = 0
    return func_count

@get_func_count
def call_one(x):
    print(f"func call one: {call_one.calls}")

@get_func_count
def call_two(x):
    print(f"func call two: {call_two.calls}")


for i in range(3):
    call_one(i)

for i in range(5):
    call_two(i)

for i in range(6):
    call_one(i)
