#!/usr/bin/python

import argparse

def find_max_profit(prices):
  sm_index = 0
  lg_index = 1

  max_profit = prices[lg_index] - prices[sm_index]
  
  for n in range(0, len(prices)):
    if prices[n] < prices[sm_index]:
      sm_index = n
      print(f'smallest: [{sm_index}] - {prices[sm_index]}')

      # print(f'sliced: {prices[-1:][0]}')

      # if prices[-1:][0] == prices[sm_index]:
      #   max_profit = 0 - prices[sm_index]
      # else:
      for i in range(sm_index + 1, len(prices) - 1):
        print(f'i: [{i}] - {prices[i]}')
        if prices[i] - prices[sm_index] > max_profit:
          print(f'prev_max: {max_profit}')
          max_profit = prices[i] - prices[sm_index]
          print(f'cur_max: {max_profit}')
    
    # if prices[n] > prices[lg_index]:
    #   lg_index = n

  return max_profit

# print(f'max_profit: {find_max_profit([10, 7, 5, 8, 11, 9])}')
print(f'max_profit: {find_max_profit([100, 90, 80, 50, 20, 10])}')
# print(f'max_profit: {find_max_profit([1050, 270, 1540, 3800, 2])}')
# print(f'max_profit: {find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])}')



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))