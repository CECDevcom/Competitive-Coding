# COMPETITIVE CODING
## PROBLEM 1
**Q.If we list all the natural numbers below 10 that are multiplies of 3 or 5,we get 3,5,6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.**

## Solution
```
sum=0
 for i in range(1,1000):
  if i%3==0 or i%5==0:
    sum+=i
print(sum) 
```
**Import time = 0.00297**
