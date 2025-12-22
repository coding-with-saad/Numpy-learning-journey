import numpy as np
arr=np.array([300,600,900])
discount=20
final_price=arr-(arr*discount)/100
print(final_price)