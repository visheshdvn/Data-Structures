# Question) Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.

# Sample Input :
# 10 
# 95 -97 -387 -435 -5 -70 897 127 23 284
# Sample Output :
# 5

def subsetSum(arr): 
      
    # NOTE: Dictonary in python in implemented as Hash Maps 
    # Create an empty hash map (dictionary) 
    hash_map = {} 
  
    # Initialize result 
    max_len = 0
  
    # Initialize sum of elements 
    curr_sum = 0
  
    # Traverse through the given array 
    for i in range(len(arr)): 
          
        # Add the current element to the sum 
        curr_sum += arr[i] 
  
        if arr[i] is 0 and max_len is 0: 
            max_len = 1
  
        if curr_sum is 0: 
            max_len = i + 1
  
        # NOTE: 'in' operation in dictionary to search  
        # key takes O(1). Look if current sum is seen  
        # before 
        if curr_sum in hash_map: 
            max_len = max(max_len, i - hash_map[curr_sum] ) 
        else: 
  
            # else put this sum in dictionary 
            hash_map[curr_sum] = i 
  
    return max_len
  
  
# test array 
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
finalLen= subsetSum(l)
print(finalLen)