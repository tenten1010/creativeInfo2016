def octToDec(oct):
	dec=0
	for i in range(len(oct)):
		dec += int(oct[i]) * 8 ** (len(oct) - 1 - i)
	print(dec)

def strToOct(oct):
	arr=[]
	dict = {"a":"0","b":"1","c":"2","d":"3","e":"4","f":"5","g":"6","h":"7"}
	for i in range(len(oct)):
		arr.append(dict[oct[i]])
	return arr

if __name__ == '__main__':
	oct = input("input a octonary string:")
	arr = strToOct(oct)
	octToDec(arr)
