def exchange(money):
    coin500 = money // 500
    money %= 500 # coin = coin % money

    coin100 = money // 100
    money %= 100

    coin50 = money // 50
    money %= 50

    coin10 = money // 10
    #money %= 10

    print("500원 동전의 개수:", coin500)
    print("100원 동전의 개수:", coin100)
    print("50원 동전의 개수:", coin50)
    print("10원 동전의 개수:", coin10)
    #print("남은 1원 단위 돈:", money)-1원 단위로 마지막까지 나눠떨어지지 않는 돈 계산

def get_integer(i):
    num = int(input(i))
    return num

cash = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(cash)
