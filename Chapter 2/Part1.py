from statistics import mean

class person():
    count = 0
    def __init__(self,age,Height,Weight):
        self.age = age
        self.Height = Height
        self.Weight = Weight
        person.count +=1
        # self.lst

    def mean(self):
        print(mean(self.age)*1.0)
        print(mean(self.Height)*1.0)
        print(mean(self.Weight)*1.0)
        # self.lst.append(mean(self.age)*1.0)
        # self.lst.append(mean(self.Height)*1.0)
        # self.lst.append(mean(self.Weight)*1.0)
        # print('################## %s' % self.lst)


class result_class():
    def __init__(self,result):
        self.result = result
    def Result_list(self):
        if self.result[1] > self.result[4]:
            print('A')
        if self.result[1] < self.result[4]:
            print('B')
        elif (self.result[1] == self.result[4]) and (self.result[2] < self.result[5]):
            print('A')
        elif (self.result[1] == self.result[4]) and (self.result[2] > self.result[5]):
            print('B')
        elif (self.result[1] == self.result[4]) and (self.result[2] == self.result[5]):
            print('Same')

#lst = [a0 , a1 , a2 , b3 , b4 , b5]
############################################################################
numbers = int(input())

age_A = list(map(int,input().split(" ")))
Height_A = list(map(int,input().split(" ")))
Weight_A = list(map(int,input().split(" ")))

class_A = person(age_A,Height_A,Weight_A)


############################################################################
numbers = int(input())

age_B = list(map(int,input().split(" ")))
Height_B = list(map(int,input().split(" ")))
Weight_B = list(map(int,input().split(" ")))

class_B = person(age_B,Height_B,Weight_B)


############################################################################

# print(class_A.mean())
# print(class_B.mean())
class_A.mean()
class_B.mean()

lst = [mean(class_A.age),mean(class_A.Height),mean(class_A.Weight),mean(class_B.age),mean(class_B.Height),mean(class_B.Weight)]
# print(lst)
return_lst = result_class(lst)
return_lst.Result_list()