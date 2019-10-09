#!/usr/bin/python

import argparse

# BUY at lowest, SELL at highest
# Max profit should be computed by subtracting some price by another price that comes before it.
# Cannot come after it in the list of prices
# find the highest price, then subtract lowest price from the numbers that came from BEFORE the highest


def find_max_profit(prices):
    # find highest price, then make a new list of everything before highest
    # Don't take index 0 as highest EVER because nothing comes before that. Always start at index 1, replace if necessary
    current_max_price_so_far = prices[1]
    # store the index of the current max price so we can make a new list later
    # it defaults to 1
    max_price_index = prices.index(current_max_price_so_far)
    # print(current_max_price_so_far, 'STARTING max price')
    # loop through prices, starting at one to avoid making current_max_price_so_far be the first value in prices
    for i in range(1, len(prices)):
      # if max price is less than whatever is at prices[i], replace max price with that value
        if current_max_price_so_far < prices[i]:
            current_max_price_so_far = prices[i]
            # also replace the index with correct number
            max_price_index = prices.index(current_max_price_so_far)
            # print(current_max_price_so_far, 'current max price')
    # create new list that holds all values before max_price_index
    # this allows us to find the min of those values and ensure it doesn't come after max price
    new_list = prices[:max_price_index]
    # print(new_list, 'NEW LIST')
    # now we have new list of viable nums we can subtract from max price. Go through this list,
    # find the lowest, and subtract
    #! If new list is ever empty, (should never be) just display this message
    if len(new_list) == 0:
        return "EMPTY"
    # default value for min price. This one is fine to be the first value as default
    current_min_price_so_far = new_list[0]
    # loop through possible min lists, find the lowest
    for j in range(0, len(new_list)):
      # replace default value with any at[j] that are smaller
        if current_min_price_so_far > new_list[j]:
            current_min_price_so_far = new_list[j]
            # print(current_min_price_so_far, 'current min price')
    # max profit will be the max - min
    max_profit = current_max_price_so_far - current_min_price_so_far
    # print(max_profit, 'MAX')
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()
    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


test_price = [1050, 270, 1540, 3800, 2]
test_price1 = [100, 90, 80, 50, 20, 10]
test_price2 = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
# print(find_max_profit(test_price))
# print(find_max_profit(test_price1))
print(find_max_profit(test_price2))
