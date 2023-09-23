import numpy as np

p = int(input("please, enter the size of the square matrix: "))

if (p > 5):
    print("the number is more then 5")
else:
    print("the number is less then or equal to 5")

a = np.zeros((p,p))
print(a)
print(type(a))

