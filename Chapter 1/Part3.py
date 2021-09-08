intnum = input ()  
num = int(intnum)

nHorror=nRomance=nComedy=nHistory=nAdventure=nAction=0

for var in list(range(num)):
    igenres=input()
    nAction=nAction+igenres.count("Action")
    nAdventure=nAdventure+igenres.count("Adventure")
    nComedy=nComedy+igenres.count("Comedy")
    nHistory=nHistory+igenres.count("History")
    nHorror=nHorror+igenres.count("Horror")
    nRomance=nRomance+igenres.count("Romance")
    
   
genre= [('Action :',nAction), ('Adventure :',nAdventure), ('Comedy :',nComedy),('History :',nHistory), ('Horror :',nHorror), ('Romance :',nRomance)]  

genre.sort(key=lambda tup:(tup[0]))#sorted alphabetically 
genre.sort(key=lambda tup:(tup[1]),reverse=True)#sorted in descending order

lnt=6
# print("Result:")

for var in list(range(lnt)):
    print(genre[var][0],genre[var][1])