def IndexWords(InputText):

    count = 2
    for i in range(len(InputText)):
        for word in InputText[i].split()[1:]:
            CapitalizationCheck = list(word.strip(','))[0].isupper()
            # print(CapitalizationCheck)
            if CapitalizationCheck == True:
                print('%s:%s' % (count, word))
                ls.append(1)
            else:
                ls.append(0)
            count += 1
        count += 1

    # print(CapitalizationCheck)
    # print(ls)
    if (CapitalizationCheck == False) and (ls == list(0 for i in range(len(ls)))):
        print('None')
ls = []
IndexWords(input().replace(','," ").split('.'))