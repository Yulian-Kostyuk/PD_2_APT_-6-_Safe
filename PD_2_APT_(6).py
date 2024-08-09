import random
import args
def password(*args, **kwargs):
    n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    number1 = random.choice(n)
    number2 = []
    for i in range(1, int(number1)):
        for j in range(2, number1):
            if number1 % (i + j) == 0:
                if i in number2[1:len(number2):2] and j in number2[0:len(number2):2] or i == j:
                    continue
                else:
                    number2.append(i)
                    number2.append(j)
            else:
                continue
    print('number1 = ', number1)
    return number2
result1 = password(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print('result = ', result1)