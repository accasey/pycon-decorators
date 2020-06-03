from pycon_decorators import timer


@timer
def waste_time(number):
    total = 0
    for num in range(number):
        total += sum(n for n in range(num))
    return total


if __name__ == "__main__":
    print('10')
    print('----------')
    print(waste_time(10))
    print('\n100')
    print('----------')
    print(waste_time(100))
    print('\n1000')
    print('----------')
    print(waste_time(1000))
    print('\n10000')
    print('----------')
    print(waste_time(10000))