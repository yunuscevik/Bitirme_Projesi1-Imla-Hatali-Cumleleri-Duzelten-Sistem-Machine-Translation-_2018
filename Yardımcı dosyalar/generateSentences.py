import os

def writeTXT(text):
	with open("test.txt", "a") as d_write:
  		d_write.write(text)
  		d_write.write("\n")
  		d_write.close()


if __name__ == "__main__":
	files = [txt for txt in os.listdir('.') if txt.endswith(".txt")]
	for file in files:
	    with open(file, "r") as d_read:
	        f = d_read.read();
	        writeTXT(" ".join(f.split()))

