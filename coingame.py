coin = 100
l = ['head', 'tail']

while True:
	from random import choice
	guess = input('Guess head or tail\n')
	ans = choice(l)

	if guess.lower() == ans:
		coin += 9
		print(coin)
	else:
		coin -= 10
		print(coin)

	if coin <= 0 or coin >=200:
		print('Game over, coin balance, ', coin)
		break
