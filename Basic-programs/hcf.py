# Program to find HCF of three numbers using Euclidean Algorithm
def hcf(a,b):
    while b !=0:
        div = a % b
        a,b = b, div
    return a

a = 12
b = 18
c = 24
# Find HCF of three numbers
result = (hcf(hcf(a,b),c))
print("HCF: ",result)