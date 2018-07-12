d = {'A':".-",
'B':"-...",
'C' :"-.-.",
'D' :"-..",
'E' :".",
'F' :"..-.",
'G':"--.",
'H' :"....",
'I' :"..",
'J' :".---",
'K' :"-.-",
'L' :".-..",
'M' :"--",	
'N' :"-.",
'O' :"---",
'P' :".--.",
'Q' :"--.-",
'R' :".-.",
'S' :"...",
'T' :"-",
'U' :"..-",
'V' :"...-",
'W' :".--",
'X' :"-..-",
'Y' :"-.--",
'Z' :"--.."}
def M_Code(l):
	nl=[]
	tstr=''
	for i in range(len(l)):
		for j in range(len(l[i])):
			s = l[i][j].upper()
			tstr+=d[s]
		nl.append(tstr)
		tstr =''
	sd={}
	for i in range(len(nl)):
		if nl[i] not in sd:
			sd[nl[i]] = 1
		else:
			sd[nl[i]]+=1
	print(nl)
	print(len(sd),"\n")


M_Code(["gin", "zen", "gig", "msg"])
M_Code(["a", "z", "g", "m"])
M_Code(["bhi", "vsv", "sgh", "vbi"])
M_Code(["a", "b", "c", "d"])
M_Code(["hig", "sip", "pot"])
