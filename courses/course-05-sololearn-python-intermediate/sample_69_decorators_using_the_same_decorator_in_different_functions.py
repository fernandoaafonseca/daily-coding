'''
Decorators are a powerful feature, offering a concise, readable, and efficient way to enhance the functionality of existing functions.

You can apply the same decorator to several different functions:
'''


def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(f'{result}: stock status for {item}')
        return result

    return wrapper


@stock_status_decorator
def restock_item(item):
    return 'Restocked'


@stock_status_decorator
def sell_item(item):
    return 'Sold'


print(restock_item('Laptop'))
print(sell_item('Smartphone'))