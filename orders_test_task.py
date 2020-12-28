ORDERS = [ {'id': '123', 'price': 0.5}, {'id': '125', 'price': 0.6}, {'id': '125', 'price': 0.4}]

def get_stat_for_orders(orders):
	min_price = find_min(orders)
	max_price = find_max(orders) 
	total_price = calculate_total_price(orders)

	avg_price_distrib = calculate_avg_price_distrib(orders)

	return min_price, max_price, avg_price_distrib, total_price

def find_min(list):
	min = list[-1]['price']
	for dict in list:
		cur = dict['price']
		if cur < min:
			min = cur
	return min

def find_max(list):
	max = list[0]['price']
	for dict in list:
		cur = dict['price']
		if cur > max:
			max = cur
	return max

def calculate_total_price(list):
	total = 0
	for dict in list:
		total += dict['price']
	return total

def calculate_avg_price_distrib(orders):

	item_stat = {}
	
	def func(dict):
		id = dict['id']
		#item = {'id': id, 'total_price': dict['price'], 'count': 1}
		if id not in item_stat:
			item_stat[id] = {'total_price': dict['price'], 'count': 1}
		else:
			item_stat[id]['total_price'] = item_stat[id]['total_price'] + dict['price']
			item_stat[id]['count'] = item_stat[id]['count'] + 1 		

	map(func, orders)

	
	avg_price_distrib = {}
	for key, value in item_stat.iteritems():
		avg_price_distrib[key] = value['total_price']/value['count']
	return avg_price_distrib

print(get_stat_for_orders(ORDERS))