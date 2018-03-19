'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''



def factor(n):
    i=2
    fac=[]
    while n>1:
        if not n%i:
            n=n/i
            fac.append(i)
        else:
            i+=1
    print max(fac)


factor(600851475143)