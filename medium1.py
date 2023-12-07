def appear(nums, n):
    res=[]
    for a in nums:
        if a not in res:
            if nums.count(a)>n//3:
                res.append(a)
    return res
  
n=int(input("nums=")) 
nums=list(map(int,input().split()))
res=appear(nums,n)
print(res)