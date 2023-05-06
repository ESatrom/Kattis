# N=int(input())
# if N>2:
#     primes=[2]
#     for i in range(3,N):
#         prime=True
#         for p in range(2,i):
#             if p*p>i:break
#             if i%p==0:
#                 prime=False
#                 break
#         if prime:primes+=[i]
#     print(len(primes))
# else:
#     print(0)

N=int(input())
primes=0
for i in range(2,N):
    prime=True
    for j in range(2,min(i//2+1,i)):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i)
        primes+=1
print(primes)