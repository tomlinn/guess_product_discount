from numpy import arange
from itertools import product
from tabulate import tabulate
item1 = 1590   # 商品1 - 價格
item2 = 550*3  # 商品2 - 價格
item3 = 450*2  # 商品3 - 價格
item4 = 0      # 商品4 - 價格

x1 = [0.72, 0.85, 1] # 商品1 - 可能的折數
x2 = [0.72, 0.85, 1] # 商品2 - 可能的折數
x3 = [0.72, 0.85, 1] # 商品3 - 可能的折數
x4 = [0.72, 0.85, 1] # 商品4 - 可能的折數

1590 + 1650 + 900 + 650

target = 4005 # 目標金額

loop_val = [x1, x2, x3, x4]
for data in product(*loop_val):
	ans = data[0]*item1 + data[1]*item2 + data[2]*item3 + data[3]*item4
	itemList = [data[0], data[1], data[2], data[3]]

	if ans >= target - 0.99 and ans <= target + 0.99 :
		
		print(tabulate([itemList], headers=['item1', 'item2', 'item3', 'item4']))
		print("總額:")
		for index,item in enumerate([item1,item2,item3,item4]):
			if item != 0:
				print(str(item)+"*"+str(data[index]), end = "") 
			if index < len(itemList)-2:
				print(" + ", end = "")
		print(" = " + str(ans))
		print()
		

