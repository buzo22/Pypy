money = input("Enter amount: ")
interest_rate = input("Enter interest rate: ")
money = float(money)


interest_rate = float(interest_rate) * 0.02

for i in range(10):
    money = money + (money * interest_rate)

print("Investment after 10years : {:.2f}".format(money))