# Python3 program to find the XOR of all elements in the array Function to find the XOR of all elements in the array 
def xorOfArray(arr, n): 
	xor_arr = 0
	for i in range(n): 
	xor_arr = xor_arr ^ arr[i] 
	return xor_arr
if __name__ == '__main__': 
arr = [3, 9, 12, 13, 15] 
n = len(arr) 
print(xorOfArray(arr, n))
