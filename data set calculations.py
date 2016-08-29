num = int(input('How many integers would you like to input? '))

data_list = []

print('Please enter your integers: ')

for i in range(num):
    x = int(input('Integer: '))
    data_list.append(x)

data_list.sort()


def data_set(data_list):
    print("Data set: ")
    for x in data_list:
        print(x,)
    print('')


def total(data_list):
    num = 0

    for x in data_list:
        num = num + x
    return num


def mean(data_list):
    num = len(data_list)
    value = 0.0

    for i in range(num):
        value = value + data_list[i]

    value = value / float(num)
    return value


def median(data_list):
    num = len(data_list)
    value = 0.0

    if num % 2 is 0:
        numx = num / 2.0
        numx = int(numx)
        value = list[numx - 1] + data_list[numx]
        value = float(value)
        value = value / 2.0

    else:
        numx = num + 1
        numx = numx / 2.0
        numx = int(numx)
        value = data_list[numx - 1]

    return value


def mode(data_list):
    num = len(data_list)
    maximum = 0
    count = 0
    numbers = []

    for i in range(1, num):
        if data_list[i] is data_list[i - 1]:
            count = count + 1

            if count is maximum:
                numbers.append(data_list[i])

            elif count > maximum:
                maximum = count
                numbers = []
                numbers.append(data_list[i])
        else:
            count = 0
    if maximum is 0:
        return 'There is no mode.'
    else:
        return numbers


def variance(data_list):
    num = len(data_list)
    mean = 0.0

    for i in range(num):
        mean = mean + data_list[i]

    mean = mean / float(num)
    total = 0.0

    for i in range(num):
        square = data_list[i] - mean
        square = square * square
        total = total + square

    final = total / num
    return final

data_set(data_list)

k = total(data_list)
print('The sum is equal to ' + str(k) + '.')

k = mean(data_list)
print('The mean is equal to ' + str(k) + '.')

k = median(data_list)
print('The median is equal to ' + str(k) + '.')

k = mode(data_list)
print('The mode is equal to ' + str(k)[1:-1] + '.')

k = variance(data_list)
print('The variance is equal to ' + str(k) + '.')

k = k ** 0.5
print('The standard deviation is equal to ' + str(k) + '.')

input('')