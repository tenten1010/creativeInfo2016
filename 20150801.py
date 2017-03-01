def fourToDec(quan):
	dec = 0
	for i in range(len(quan)):
		dec += int(quan[i]) * 4 ** (len(quan) - 1 - i)

	print("result is %d"%dec)

if __name__=="__main__":
	quan = input("input a quanternary number:")
	fourToDec(quan)
