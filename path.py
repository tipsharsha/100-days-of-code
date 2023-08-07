def path(n,m):
    if n ==1 or m == 1:
      return 1
    else: 
        return path(n-1,m)+path(n,m-1)
print(path(2,3))
