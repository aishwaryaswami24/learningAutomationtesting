# s = "a4b3c2"
# output = aaaabbbcc


#find out frequency of str
str='this is manali and i loved manali'
lst=str.split()
dict={}

for i in lst:
    if i not in dict.keys():
        dict[i]=0
    dict[i]=dict[i]+1
print(dict)