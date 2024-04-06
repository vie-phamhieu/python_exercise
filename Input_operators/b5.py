def check_input_number():
    while True:
        try:
            number = int(input('Nhập vào số nguyên cần kiểm tra: '))
            return number
        except ValueError:
            print('Nhập sai. Vui lòng nhập số nguyên.')

def check_user_want_to_continue_or_not():
    while True:
        user_decision = input('Bạn có muốn tiếp tục kiểm tra hay không? (yes/no): ').lower()
        if user_decision in ['no', 'n']:
            return False
        elif user_decision in ['yes', 'y']:
            return True
        else:
            print('Vui lòng nhập "yes" hoặc "no".')

def is_divisible_by_3_and_in_range(num):
    return num % 3 == 0 and 50 <= num <= 100

def main():
    while True:
        num = check_input_number()
        result = is_divisible_by_3_and_in_range(num)
        if result:
            print(f'{num} là số nguyên chia hết cho 3 và nằm trong khoảng từ 50 đến 100.')
        else:
            print(f'{num} không thỏa mãn điều kiện.')
        if check_user_want_to_continue_or_not() is False:
            break

if __name__ == "__main__":
    main()
