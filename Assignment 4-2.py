#Assignment 4-2 by Diego Suarez

book_shop_orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80], 
    [77226, "Head First Python, Paul Barry", 3, 32.95], [
    88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

order_product = lambda x: (x[0], x[2] * x[3])
order_totals = list(map(order_product, book_shop_orders))

add_10 = lambda x: x if x[1] >= 100 else (x[0], x[1] + 10)

order_totals_adjusted = list(map(add_10, order_totals))

print(order_totals_adjusted)

from functools import reduce

book_shop_orders2 = [ 
    [1, (34587, 4, 40.95), (88112, 18, 24.99), (98762, 9, 56.80)],
    [2, (56832, 9, 19.99), (98762, 3, 56.80)],
    [3, (54321, 19, 7.99), (88112, 11, 24.99)],
    [4, (89772, 7, 16.99), (77226, 11, 32.95), (88112, 5, 24.99)] 
]

product = lambda y: y[1] * y[2]
sum_operation = lambda a, b: a + b

reduced_order_totals = list(map(lambda x: (x[0], reduce(sum_operation, list(map(product, x[1:])))),book_shop_orders2))

print(reduced_order_totals)