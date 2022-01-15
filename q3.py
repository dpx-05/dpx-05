#Assignment-1: Operators | Loops

#Write a Python program to count the number of even and odd numbers from a series of numbers.

n = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
sum_odd = 0
sum_even = 0
for x in n:
        if not x % 2:
    	    sum_even+=1
        else:
    	    sum_odd+=1
print("Number of even numbers :",sum_even)
print("Number of odd numbers :",sum_odd)