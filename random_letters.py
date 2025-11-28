import random
import string
import time

def letterprint():
	i = 0
	while i == 0:
		ascii_block1 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block2 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block3 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block4 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block5 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block6 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block7 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block8 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block9 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block10 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block11 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block12 = ''.join(random.sample(string.ascii_lowercase, 26))
		ascii_block13 = ''.join(random.sample(string.ascii_lowercase, 26))
		print(ascii_block1, ascii_block2, ascii_block3, ascii_block4, ascii_block5, ascii_block6, ascii_block7, ascii_block8, ascii_block9, ascii_block10, ascii_block11, ascii_block12, ascii_block13)
		sleep()		

def sleep():
	time.sleep(0.3)

def main():
	letterprint()
	
if __name__ == "__main__":
	main()









        	
        
       
      
     
    











