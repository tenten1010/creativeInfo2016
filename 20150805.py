def decToArr(dec):
	arr = []
	numDec = int(dec)
	for i in range(len(dec)):
		arr.append(int(dec[i]) * 10 ** (len(dec)-1-i))
	return arr

def arrToRoma(arr):
	romaDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	decDict = {value:key for key,value in romaDict.items()}
	str=""
	for i in range(len(arr)):
		figure = int(10 **(len(arr)-1-i))
		if (arr[i] % (5*figure))/figure <4:
			str += int((arr[i]/figure))*decDict[figure] if arr[i] < (5*figure) else decDict[5*figure]+int((arr[i]/figure)-5)*decDict[figure]
		else:
			str += decDict[figure]+decDict[5*figure] if arr[i] < (5*figure) else decDict[figure]+decDict[10*figure]
	print(str)

if __name__ == "__main__":
	dec = input("input a number:")
	if( 0 < int(dec) < 4000):
		arr = decToArr(dec)
		arrToRoma(arr)
	else:
		print("supposed to be smaller than 4000")