number = int(input())
lis = []


for i in range(number):
    arr = list(map(str, input().split('.')))
    lis.extend(arr)

item = [i for i, e in enumerate(lis) if (e == 'm') or (e == 'f')]
# print(item)
for j in range(len(item)):
    # lis[item[j]+1].lower()
    lis[item[j]+1] = lis[item[j]+1].capitalize()

new_list = [lis[i:i+3] for i in range(0, len(lis), 3)]

# item = [i for i, e in enumerate(lis) if e == 'f']
# if len(item)>1:
  
# for j in range(len(item)):
#     print(f'{lis[item[j]]} {lis[item[j]+1]} {lis[item[j]+2]}')

# item = [i for i, e in enumerate(lis) if e == 'm']
# for j in range(len(item)):
#     print(f'{lis[item[j]]} {lis[item[j]+1]} {lis[item[j]+2]}')

# print(new_list)

# print(new_list)
for i in range(number):
    for j in range(number):
        if not((new_list[i][0] > new_list[j][0])) and (i != j):
            new_list[i], new_list[j] = new_list[j],new_list[i]

for i in range(number):
    for j in range(number):
        if not((new_list[i][1] > new_list[j][1])) and (i != j) and (new_list[i][0] == 'f'):
            new_list[i], new_list[j] = new_list[j],new_list[i]
        elif not((new_list[i][1] > new_list[j][1])) and (i != j) and (new_list[i][0] == 'm'):
            new_list[i], new_list[j] = new_list[j],new_list[i]


for i in range(number):
    if new_list[i][0]=='f':
        print(f'{new_list[i][0]} {new_list[i][1]} {new_list[i][2]}')

for i in range(number):
    if new_list[i][0]=='m':
        print(f'{new_list[i][0]} {new_list[i][1]} {new_list[i][2]}')

# print(new_list)


# f Mina C
# f Mina C
#    
# f Sara java
# f Sara java


# m Ahmad C++
# m Ahmad C++


# m Hossein python
# m Hossein python



# f Mina C
# f Sara java
# m Ahmad C++
# m Hossein python