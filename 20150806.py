def getFourNine(dec):
	result = 0
	dec = dec[::-1]
	for i in range(len(dec)):
		if dec[i] == "9":
			result += 9 * 10 ** i
			if i+1 < len(dec):
				if dec[i+1] == "4":
					result += 4 * 10 ** (i+1)
					break
				elif dec[i+1] == "9":
					continue
				else:
					break
	return result

def makeArr(dec):
	arr = []
	numDec = int(dec)
	for i in range(len(dec)):
		if dec[i] != "0":
			arr.append([(int(dec[i]) * 10 ** (len(dec)-1-i)),0])
	return arr

def combineArr(arr,fourNine):
	for num in fourNine:
		for i in range(len(arr)):
			if num < arr[i][0]:
				arr.insert((i+1),[num,1])
				break
	arr = sorted(arr)
	arr = arr[::-1]
	return arr
	
def toRoma(num):
	result=""
	numString = str(num)
	figure = 10 ** (len(numString)-1)
	if (num % (5*figure))/figure <4:
		result += int((num/figure))*decDict[figure] if num < (5*figure) else decDict[5*figure]+int((num/figure)-5)*decDict[figure]
	else:
		result += decDict[figure]+decDict[5*figure] if num < (5*figure) else decDict[figure]+decDict[10*figure]
	return result

def minusRoma(num):
	result = ""
	figure = 5 * 10 ** (len(str(num))-1)
	result += decDict[figure-num]
	result += decDict[figure]
	return result

def decToRoma(dec):
	nvDec = dec
	fourNine = []
	arr = []
	result=""
	while getFourNine(nvDec) != 0:
		fourNine.append(getFourNine(nvDec))
		nvDec = str(int(nvDec) - getFourNine(nvDec))
	arr = makeArr(nvDec)
	arr = combineArr(arr,fourNine)
	for index in arr:
		if index[1] == 0:
			result += toRoma(index[0])
		else:
			result += minusRoma(index[0])
	print(result)

if __name__ == '__main__':
	romaDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	decDict = {value:key for key,value in romaDict.items()}
	dec = input("input a number:")
	# getFourNine(dec)
	decToRoma(dec)
