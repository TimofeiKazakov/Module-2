def find_password(number):
    password = []
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password


print('3 =' , *find_password(3))
print('4 =' , *find_password(4))
print('5 =' , *find_password(5))
print('6 =' , *find_password(6))
print('7 =' , *find_password(7))
print('8 =' , *find_password(8))
print('9 =' , *find_password(9))
print('10 =' , *find_password(10))
print('11 =' , *find_password(11))
print('12 =' , *find_password(12))
print('13 =' , *find_password(13))
print('14 =' , *find_password(14))
print('15 =' , *find_password(15))
print('16 =' , *find_password(16))
print('17 =' , *find_password(17))
print('18 =' , *find_password(18))
print('19 =' , *find_password(19))
print('20 =' , *find_password(20))