products = []
while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input('please enter price: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)
