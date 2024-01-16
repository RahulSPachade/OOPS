# l1 = []
# for i in range(1,51):
#   if i % 5 == 0:
#     l1.append(i)
#   else:
#     print("The Number is Not Divisible")
# print(f"The {i} is Divisible by 5!!! {l1}")

l4 = [1,2,4,5,7,9]
res = []
for i in range(l4[0],l4[-1]+1):
  if i not in l4:
    res.append(i)
print(res)    

# result = [res.append(x) for x in l1 if x not in l1]
# print(res)  

l2 = [1,1,2,2,3,4,5,6]
res1 = []
for i in l2:
  if i not in res1:
    res1.append(i)
# print(res1)      