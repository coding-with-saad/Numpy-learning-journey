price=[200,400,600,800,1000]
discount=20

final=[]

for p in price:
    d=p*discount/100
    final_price=p-d
    final.append(final_price)

print(final)
