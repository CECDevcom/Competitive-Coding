# COMPETITIVE CODING
## PROBLEM 1
**Q.If we list all the natural numbers below 10 that are multiplies of 3 or 5,we get 3,5,6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.**
## SOLUTION
```
sum=0
 for i in range(1,1000):
  if i%3==0 or i%5==0:
    sum+=i
print(sum) 
```
**Import time = 0.00297**

## PROBLEM 2
**Q.Each new term in the fibonacci sequence is generated by adding the previous two terms.By starting with 1 and 2,the first 10 terms will be : 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...By considering the terms in the Fibonacci sequence Whose values do not exceed four million, find the sum of the even-valued terms.**
## SOLUTION
```
def li(limit):
    a,b=0,1
    while a<limit:
      if not a%2:
        yield a
      a,b=b,a+b
  print (sum(li(4000000)))
```
**Import time =0.04**

## PROBLEM 3
**Q.The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143 ?**
## SOLUTION
```
def factor(n):
    i=2
    fac=[]
    while n>1:
        if not n%i:
            n=n/i
            fac.append(i)
        else:
            i+=1
    print (max(fac))
factor(600851475143)
```
**Import time = 0.01**
