dic = {}
for i in range(10):   
    c = 0
    n = int(input())
    for i in range(2,n + 1):
        if n % i == 0:
            count = 1
            for j in range(2,(i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                c = c + 1
            # print(i)
    # print(c)
    new_key_values_dict = {n:c}
    dic.update(new_key_values_dict)

# print(dic)
max_value = max(dic.values())  # maximum value
max_keys = max([k for k, v in dic.items() if v == max_value]) # getting all keys containing the `maximum`

print(max_keys,max_value)