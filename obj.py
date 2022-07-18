def square(number):
    return number * number

num = 2
sqnum = square(num)
sqnumber = square
sqnum=sqnumber(2)
print(sqnum)

#map higher-order function
numbers = [1, 2, 3, 4]
numbersq = list(map(square, numbers))
print(numbersq)