'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''




'''The initial Solution


sum=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)

'''


'''The New Solution'''
sum=0
n=1000/3
sum=3*n*(n+1)/2
n=1000/5
sum+=5*n*(n+1)/2

n=1000/15
total=sum-(15*n*(n+1)/2)
print total

