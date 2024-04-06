# Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False

def check_number():
    while True:
        try:
            number = int(input('Nhập vào số nguyên cần kiểm tra: '))
            return number
        except ValueError:
            print('Nhập sai. Vui lòng nhập số nguyên.')

def is_divisible_by_2(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    while True:
        number = check_number()
        result = is_divisible_by_2(number)
        print(f'Số {number} chia hết cho 2: {result}')
        while True:
            user_decision = input('Bạn có muốn tiếp tục kiểm tra hay không? (yes/no): ').lower()
            if user_decision in ['yes', 'y']:
                break
            elif user_decision in ['no', 'n']:
                return
            else:
                print('Vui lòng nhập "yes" hoặc "no".')

if __name__ == '__main__':
    main()

    main()