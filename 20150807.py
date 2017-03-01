engDict = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"forteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":"20","thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,"hundred":100,"thousand":1000}

def engToDec(eng):
	arr = eng.split(' ')
	result = 0
	for i in range(len(arr)):
		if arr[i] == "thousand" or arr[i] == "hundred":
			result *= int(engDict[arr[i]])
		else:
			result += int(engDict[arr[i]])
	print(result)

if __name__ == '__main__':
	eng = input("input:")
	engToDec(eng)