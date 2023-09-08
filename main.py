# 1.1 Implement s a recursive function to calculate the factorial to a given number

def fact_rec(n):
   if n==0 or n==1:
      return 1
   else:
     return n*fact_rec(n-1)

number=2
res=fact_rec(number)

print("The factoiral of {} is {}".format (number,res))