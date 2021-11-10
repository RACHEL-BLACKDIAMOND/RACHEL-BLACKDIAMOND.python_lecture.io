#aa = [10, 20, 30, 40]
#hap = 0

#aa[0] = int(input("1번째 숫자 :"))
#aa[1] = int(input("2번째 숫자 :"))
#aa[2] = int(input("3번째 숫자 :"))
#aa[3] = int(input("4번째 숫자 :"))

#hap = aa[0]+aa[1]+aa[2]+aa[3]

#print(f'합계 : {hap}')

#------------------------------------

aa=[]
bb=[]
value=0

for i in range(0,100) :
    aa.append(value)
    value+=2

for i in range(0,100) :
    bb.append(aa[99-i])

print(f'bb[0]에는 {bb[0]}이, bb[99]에는 {bb[99]}값이 출력됩니다.')    
    