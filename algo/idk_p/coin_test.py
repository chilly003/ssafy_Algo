#거스름돈 문제
money = 5670
changes = [1000,500,100,50,10]
coin =[]

#각 돈 단위별로 몇개씩 고객에게 줘야할지?

for changes in changes:
    mok, res = divmod(money, changes) #내장 함수 몫과 나머지를 각각 반환해준다.
    print(changes,mok)
    money = res
    if money == 0:
        break

