S,N=[int(i)for i in input().split()]
print(sum((1 if x==N/x else 2)if N/x==N//x and N/x<=S else 0 for x in range(1,1+min(int(N**.5),S))))