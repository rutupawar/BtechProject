#Main task file

# Python program to illustrate the use 
# of fast Input / Output 
import io, os, time 

st = ""
# Function to take normal input 
def normal_io(): 
	
	# Stores the start time 
	start = time.perf_counter() 
	
	# Take Input 
	st = input("Enter file to be scanned: ").strip();
	
	# Stores the end time 
	end = time.perf_counter()
	
	# Print the time taken 
	print("\nTime taken in Normal I / O:",end - start)

# Function for Fast Input 
def fast_io(): 
	
	# Reinitialize the Input function 
	# to take input from the Byte Like 
	# objects 
	input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline 

	# Fast Input / Output 
	start = time.perf_counter() 

	# Taking input as string 
	s = input().decode() 
	
	# Stores the end time 
	end = time.perf_counter() 

	# Print the time taken 
	print("\nTime taken in Fast I / O:",end - start) 

# Driver Code 
if __name__ == "__main__": 

	# Function Call 
	normal_io() 
	
	fast_io() 


#array to store bytes of file
byte_list = []


#file to be opened for byte representation
with open("sample.txt", "rb") as f:
    while True:
    #traversing whole file
        byte = f.read(1)
        if not byte:
        	#Encountered end of file
            break
        # Add scanned byte to array
        byte_list.append(byte)


# priting chars in file; only for text files
print(byte_list)

# View byte representation of file
for byte in byte_list:
    int_value = ord(byte)
    #formatting of string to decimal
    binary_string = '{0:08b}'.format(int_value)
    print(binary_string)
    
    
