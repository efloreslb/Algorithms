#!/usr/bin/python

import argparse

def find_max_profit(prices):

  sm_index = 0
  lg_index = 1
  
  for n in range(0, len(prices)):
    if prices[n] < prices[sm_index]:
      sm_index = n
    
    if prices[n] > prices[lg_index]:
      lg_index = n
  
  max_profit = prices[lg_index] - prices[sm_index]

  return max_profit

print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))