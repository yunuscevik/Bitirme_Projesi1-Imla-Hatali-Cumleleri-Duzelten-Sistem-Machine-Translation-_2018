import os
import random
import csv

def writeTXT(text):
	with open("test.txt", "a") as d_write:
  		d_write.write(text)
  		d_write.write(" ")
  		d_write.close()


def checkText(lists):
	for text in lists:
		if (1 < len(text)-1):
			switcher_function(random.randrange(0,6),text)
		else:
			writeTXT(text)
		
def switcher_function(argument, text):
    if(argument == 0):
        writeTXT(replaceAlphabet(text))
    elif(argument == 1):
        writeTXT(addAlphabet(text))
    elif(argument == 2):
        writeTXT(dropVowelAlphabet(text))
    elif(argument == 3):
        writeTXT(dropConsonantAlphabet(text))
    else:
    	writeTXT(text)
    

			
def addAlphabet(text):
	textList = list(text)
	piece = round(len(text) * 0.15)
	for i in range(piece):
		rand = random.randrange(len(textList)-1)
		if textList[rand].isalpha():
			textList.insert(rand+1,textList[rand])	
	return ''.join(textList)

def dropVowelAlphabet(text):
	flag = 1
	retVal = ""
	vowel = "aeıioöuüAEIİOÖUÜ"
	for char in text:
		if not char in vowel:
			retVal += char
		if(flag == 1):
			if char in vowel:
				retVal += char
				flag = 0
	return retVal


def dropConsonantAlphabet(text):
	tempText = ""
	textList = list(text)
	vowel = "aeıioöuüAEIİOÖUÜ"
	for i in range(1, len(textList)-1):
		if not textList[i] in vowel:
			tempText += textList[i]
	piece = round(len(tempText) * 0.15)
	for i in range(piece):
		flag = 1
		rand = random.randrange(1,len(textList)-1)
		for j in range(0, len(textList)):
			if(flag == 1):
				if not textList[rand] in vowel and textList[rand].isalpha():
					textList.remove(textList[rand])
					flag = 0
				else:
					rand = random.randrange(1,len(textList)-1)
	return ''.join(textList)

	

def replaceAlphabet(text):
	textList = list(text)
	piece =round(len(text) * 0.15)
	rand = random.sample(range(0, len(text)-1), piece)
	for i in rand:
		if textList[i].isalpha():
			textList[i] = sameAlphabet(textList[i])
	return ''.join(textList)

def sameAlphabet(char):
	if(char == "a"):
		sAlphabet = "qwsz"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "A"):
		sAlphabet = "QWSZ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "b"):
		sAlphabet = "vghn"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "B"):
		sAlphabet = "VGHN"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "c"):
		sAlphabet = "xdfv"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "C"):
		sAlphabet = "XDFV"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "ç"):
		sAlphabet = "ölş"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Ç"):
		sAlphabet = "ÖLŞ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "d"):
		sAlphabet = "erfcxs"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "D"):
		sAlphabet = "ERFCXS"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "e"):
		sAlphabet = "wsdfr"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "E"):
		sAlphabet = "WSDFR"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "f"):
		sAlphabet = "rtgvcd"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "F"):
		sAlphabet = "RTGVCD"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "g"):
		sAlphabet = "tyhbvf"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "G"):
		sAlphabet = "TYHBVF"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "ğ"):
		sAlphabet = "pşiü"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Ğ"):
		sAlphabet = "PŞİÜ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "h"):
		sAlphabet = "yujnbg"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "H"):
		sAlphabet = "YUJNBG"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "ı"):
		sAlphabet = "ujklo"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "I"):
		sAlphabet = "UJKLO"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "i"):
		sAlphabet = "üğş"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "İ"):
		sAlphabet = "ÜĞŞ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "j"):
		sAlphabet = "uıkmnh"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "J"):
		sAlphabet = "UIKMNH"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "k"):
		sAlphabet = "ıolömj"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "K"):
		sAlphabet = "IOLÖMJ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "l"):
		sAlphabet = "opşçök"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "L"):
		sAlphabet = "OPŞÇÖK"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "m"):
		sAlphabet = "njkö"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "M"):
		sAlphabet = "MKLÇ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "n"):
		sAlphabet = "bhjm"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "N"):
		sAlphabet = "BHJM"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "o"):
		sAlphabet = "ıklşp"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "O"):
		sAlphabet = "IKLŞP"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "ö"):
		sAlphabet = "mklç"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Ö"):
		sAlphabet = "MKLÇ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "p"):
		sAlphabet = "olşiğ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "r"):
		sAlphabet = "edfgt"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "R"):
		sAlphabet = "EDFGT"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "s"):
		sAlphabet = "wedxza"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "S"):
		sAlphabet = "WEDXZA"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "ş"):
		sAlphabet = "pğiçl"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Ş"):
		sAlphabet = "PĞİÇL"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "t"):
		sAlphabet = "rfghy"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "T"):
		sAlphabet = "RFGHY"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "u"):
		sAlphabet = "yhjkı"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "U"):
		sAlphabet = "YHJKI"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "ü"):
		sAlphabet = "ği"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Ü"):
		sAlphabet = "Ğİ"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "v"):
		sAlphabet = "cfgb"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "V"):
		sAlphabet = "CFGB"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "y"):
		sAlphabet = "tghju"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Y"):
		sAlphabet = "TGHJU"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "z"):
		sAlphabet = "asx"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Z"):
		sAlphabet = "ASX"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "w"):
		sAlphabet = "qasde"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "W"):
		sAlphabet = "QASDE"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "x"):
		sAlphabet = "zsdc"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "X"):
		sAlphabet = "ZSDC"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "q"):
		sAlphabet = "wsa"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	elif(char == "Q"):
		sAlphabet = "WSA"
		retVal = sAlphabet[random.randrange(0,len(sAlphabet))]
		return retVal
	else:
		return char



def bozma(text):
	List = []
	List = text.split()
	checkText(List)



if __name__ == "__main__":
    with open("dataset.csv") as csvfile:
    	readCSV = csv.reader(csvfile, delimiter='\n')
    	for row in readCSV:
        	bozma(" ".join(row))
        	writeTXT("\n")
        

