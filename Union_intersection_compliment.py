#write an program to find union intersection and complicated of fuzzy set
dict1={}
keys=[]
dict2={}
num=int(input("Enter total no of keys:"))
for i in range(num):
    key=input("Enter key")
keys.append(key)

for key in keys:
    value1 = input(f"Enter a value for fuzzy set 1 '{key}': ")
    dict1[key] = value1
for key in keys:
    value2 = input(f"Enter a value for fuzzy set 2 '{key}': ")
    dict2[key] = value2
print(keys,dict1,dict2)
