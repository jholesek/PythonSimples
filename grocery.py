#7 lines: Dictionaries, generator expressions

prices: dict = {'apple': 0.40, 'banana': 0.50}

my_purchase: dict = {
	'apple':1,
	'banana':6}
grocery_bill=sum(prices[fruit] * my_purchase[fruit]
			for fruit in my_purchase)
print('My grocerry bill is $%.2f' % grocery_bill)


