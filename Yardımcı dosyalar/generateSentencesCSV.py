import os
import csv

def writeTXT(text):
	with open("test.txt", "a") as d_write:
  		d_write.write(text)
  		d_write.write(" ")
  		d_write.close()



def bozma(text):
	List = []
	List = text.split()
	checkText(List)



if __name__ == "__main__":
    with open("dataset.csv") as csvfile:
    	readCSV = csv.reader(csvfile, delimiter='\n')
    	for row in readCSV:
    		print(row)
        	#bozma(" ".join(row))
        	#writeTXT("\n")
        

