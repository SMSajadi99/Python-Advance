from operator import itemgetter
n = 6
lis = []

for i in range(n):
    arr = list(map(int, input().split('-')))
    lis.extend(arr)

# print(lis)
# [2, 2, +
#  2, 1, +
#  1, 2,  +
#  2, 2, +
#  3, 1,
#  2, 1]
# iran spain /  iran por / iran mara / spain por / spain mar / por mar

win_iran = win_spain = win_por = win_mar = 0
los_iran = los_spain = los_por = los_mar = 0
draw_iran = draw_spain = draw_por = draw_mar = 0
dif_iran = dif_spain = dif_por = dif_mar = 0
point_iran = point_spain = point_por = point_mar = 0

if lis[0] > lis[1]:
    win_iran +=1
    los_spain +=1
elif lis[0] == lis[1]:
    draw_iran +=1
    draw_spain +=1
elif lis[0] < lis[1]:
    win_spain +=1
    los_iran +=1

###################################################

if lis[2] > lis[3]:
    win_iran +=1
    los_por +=1
elif lis[2] == lis[3]:
    draw_iran +=1
    draw_por +=1
elif lis[2] < lis[3]:
    win_por +=1
    los_iran +=1

###################################################
    
if lis[4] > lis[5]:
    win_iran +=1
    los_mar +=1
elif lis[4] == lis[5]:
    draw_iran +=1
    draw_mar +=1
elif lis[4] < lis[5]:
    win_mar +=1
    los_iran +=1


###################################################


if lis[6] > lis[7]:
    win_spain +=1
    los_por +=1
elif lis[6] == lis[7]:
    draw_spain +=1
    draw_por +=1
elif lis[6] < lis[7]:
    win_por +=1
    los_spain +=1

###################################################


if lis[8] > lis[9]:
    win_spain +=1
    los_mar +=1
elif lis[8] == lis[9]:
    draw_spain +=1
    draw_mar +=1
elif lis[8] < lis[9]:
    win_mar +=1
    los_spain +=1


###################################################


if lis[10] > lis[11]:
    win_por +=1
    los_mar +=1
elif lis[10] == lis[11]:
    draw_por +=1
    draw_mar +=1
elif lis[10] < lis[11]:
    win_mar +=1
    los_por +=1

############################################

point_iran = win_iran*3 + draw_iran
point_spain = win_spain*3 + draw_spain
point_mar = win_mar*3 + draw_mar
point_por = win_por*3 + draw_por


###################################################



dif_iran = lis[0] + lis[2] + lis[4] - (lis[1] + lis[3] + lis[5])
dif_spain = lis[1] + lis[6] + lis[8] - (lis[0] + lis[7] + lis[9])
dif_por = lis[3] + lis[7] + lis[10] - (lis[2] + lis[6] + lis[11])
dif_mar = lis[5] + lis[9] + lis[11] - (lis[4] + lis[8] + lis[10])

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


x = [['Iran',win_iran,los_iran,draw_iran,dif_iran,point_iran],['Spain',win_spain,los_spain,draw_spain,dif_spain,point_spain],['Portugal',win_por,los_por,draw_por,dif_por,point_por],['Morocco',win_mar,los_mar,draw_mar,dif_mar,point_mar]]
# print(x)

# win los draw dif poitn
x = sorted(x, key=lambda i:i[5], reverse=True)
# print(x)

for i in range(4):
    for j in range(4):
        if (x[i][5] == x[j][5]) and (i != j) and (x[i][1] < x[j][1]):
            x[i], x[j] = x[j],x[i]


        elif (x[i][5] == x[j][5]) and (i != j) and (x[i][1] == x[j][1]) and not((x[i][0].lower() > x[j][0].lower())):
            x[i], x[j] = x[j],x[i]


for i in range(4):
    print(f'{x[i][0]}  wins:{x[i][1]} , loses:{x[i][2]} , draws:{x[i][3]} , goal difference:{x[i][4]} , points:{x[i][5]}')
