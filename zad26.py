A=int(input("Введите A "))
B=int(input("Введите B "))
def func(A,B):
    if B==0:
        return 1
    return A * func(A,B - 1)
print (func(A,B))