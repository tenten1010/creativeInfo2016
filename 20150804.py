def romaToDec(roma):
	dec = 0
	romaDict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	for i in range(len(roma)):
		if i>1 and romaDict[roma[i]]>romaDict[roma[i-1]]:
			dec -= 2*romaDict[roma[i-1]]
		dec += romaDict[roma[i]]
	print(dec)

if __name__ == "__main__":
	roma = input("input a roma number:")
	romaToDec(roma)

