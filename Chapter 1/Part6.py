from collections import defaultdict

n = int(input())
tran = {}
name = []

for i in range(n):
    x=input()
    x=x.split()
    name.extend(x)

# print(name)

def Convert(lst):
    res_dct = {(lst[i+1],lst[i+2],lst[i+3]): lst[i] for i in range(0, len(lst), 4)}
    return res_dct


lst = Convert(name)

# print(lst)


t = input()
t=t.split()
h = []


dIndex = defaultdict(list)
[dIndex[k].append(t) for t in lst for k in t]

keysWith2 = []
newList = []

for i in t:
    keysWith2.append(dIndex[i])
    valuesOf2 = [lst[j] for j in dIndex[i]]
    if (dIndex[i] == []):
        valuesOf2 = i
    newList.append(valuesOf2)



    # print(newList)
    # print(i)
    # print('$#%$%$%$%$%$')
    # print(valuesOf2)
    # print('$#%$%$%$%$%$')
    # print(dIndex[i])
    # print('$#%$%$%$%$%$')

# print(newList)

# for i in t:
#     h.append(lst.get(i,i))

# print(' '.join(h))


res = [''.join(ele) for ele in newList]

  
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
        
# s = ['Geeks', 'for', 'Geeks']
print(listToString(res))

####################################################################

# c=dict()
# x=int(input())
# for i in range(x):
#     y=input()
#     l=y.split()
#     c[l[0]]=l[1]
# m=[]
# t=input()
# t=t.split()
# for j in t:
#  m.append(c.get(j,j))
# print(' '.join(m))