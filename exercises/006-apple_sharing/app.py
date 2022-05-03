#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 
def apple_sharing(n,k):
  quotient,remainderApples = divmod(k,n)
  
  return f"Each student will get {quotient} apples, and {remainderApples} will be left over in the basket"
 
    

#Print the two answer per the example output.
print(apple_sharing(6,50))