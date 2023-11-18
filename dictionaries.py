dict1={'StdNo':'523','StuName':'manikanta','StuAge':28,'StuCity':'Hyderabad'}
print("\n Dictionary is:",dict1)
print("\n Student Name is:",dict1['StuName'])
print("\n Student City is:",dict1['StuCity'])
print("\n All keys in Dictionary")
for x in dict1:
    print(x)
print("\n All Values in Dictionary")
for x in dict1:
    print(dict1[x])
dict1["Phno"]=9542090802
dict1["StuName"]="siva"
print("\n Updated Dictionary is:",dict1)
dict1.pop("StuAge");
print("\n Updated Dictionary :",dict1)
print("Length of Dictionary is:",len(dict1))
dict2=dict1.copy()
print("\n New Dictionary is:",dict2)
dict1.clear()
print("\n Updated Dictionary is:",dict1)

