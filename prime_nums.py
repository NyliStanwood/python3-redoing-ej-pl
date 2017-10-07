def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, num):
            if num % i == 0:
                return False

    return True


def run():
    num = int(input('give me a num:'))
    res = is_prime(num)
    if res is True:
        print('your number is prime')
    else:
        print('not prime')

if __name__ == '__main__':
    run()
