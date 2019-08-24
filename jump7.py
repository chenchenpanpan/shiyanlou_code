
#coding=utf-8
for i in range(1,101):
    #print(i,type(i))
    if i % 7 == 0:
        continue
    elif i%10 == 7:
        continue
    elif i // 10==7:
        continue
    else:
        print(i)

