# Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
def check_input_number():
    while True:
        try:
            number_1 = int(input('Nhập vào số nguyên cần kiểm tra: '))
            number_2 = int(input("Nhập vào một số khác: "))
            return number_1, number_2
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

def is_divisible_by_2(num_1, num_2):
    if num_1 % 2 == 0 or num_2 % 2 == 0:
        return True
    else:
        return False
    
def main():
    while True:
        num_1, num_2 = check_input_number()
        result = is_divisible_by_2(num_1, num_2)
        if result:
            print(f'Ít nhất một trong hai số chia hết cho hai.')
        else:
            print(f'Cả hai số đều không chia hết cho 2.')
        if not check_user_want_to_continue_or_not():
            break

if __name__ == "__main__":
    main()

# Một function khác in ra result chi tiết hơn
'''

def is_divisible_by_2(num_1, num_2):
    div_1 = 'chia hết cho 2' if num_1 % 2 == 0 else None
    div_2 = 'chia hết cho 2' if num_2 % 2 == 0 else None

    if div_1 and div_2:
        print(f'Cả {num_1} và {num_2} đều {div_1}')
    elif div_1:
        print(f'{num_1} {div_1}')
    elif div_2:
        print(f'{num_2} {div_2}')
    else:
        print('Không có số nào chia hết cho 2')

def main():
    while True:
        num_1, num_2 = check_input_number()
        is_divisible_by_2(num_1, num_2)
        if not check_user_want_to_continue_or_not():
            break

if __name__ == "__main__":
    main()

'''

