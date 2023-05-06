nums=[int(input())for i in range(int(input()))]
big=max(nums)

pos = [True for x in range(big)]

i = 2
primes = [2]
x=2
while x*2 < len(pos):
    pos[x*2]=False
    x+=1

while i*i <= big:
    i+=1
    if pos[i]==False:continue
    prime = True
    for p in primes:
        if i%p==0:
            prime=False
            break
    if prime:
        primes+=[i]
        x=i
        while x*i < len(pos):
            pos[x*i]=False
            x+=1

primes = list(filter(lambda x: pos[x], range(2,big)))

for num in nums:
    res = []
    i=0
    while primes[i]<=num/2:
        if num-primes[i] in primes:
            res+=[str(primes[i])+"+"+str(num-primes[i])]
        i+=1
    print(str(num)+" has "+str(len(res))+" representation(s)")
    print('\n'.join(res)+'\n')