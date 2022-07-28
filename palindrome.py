# x = input('enter the number')
# def pali(x1):
#     x = x1
#     num = 0
#     while x != 0:        
#         num = x%10 + num*10
#         x = x // 10
#     if num == x1:
#         return True
#     else:
#         return False
# print(pali(x))

# Aobove code is slow hence we use below code for speed

x = input('enter the number')
def pali(x):
    if x == x[::-1]:
        return True
    else:
        return False
print(pali(x))