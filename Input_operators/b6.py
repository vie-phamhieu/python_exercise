# Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
def check_number():
    while True:
        try:
            number = int(input('Nhập vào số nguyên cần kiểm tra: '))
            return number
        except ValueError:
            print('Không phải số nguyên, vui lòng nhập lại')

def is_divisible_by_5_and_not_in_range(num):
    if num % 5 == 0 and (num < 20 or num > 70):
        return True
    else:
        return False

def main():
    while True:
        num = check_number()
        result = is_divisible_by_5_and_not_in_range(num)
        if result:
            print(f'{num} là số nguyên chia hết cho 5 nhưng không nằm trong khoảng từ 20 đến 70.')
        else:
            print(f'{num} không chia hết cho 5 hoặc nằm trong khoảng từ 20 đến 70.')
        user_decision = input('Bạn có muốn tiếp tục kiểm tra hay không? (yes/no): ').lower()
        if user_decision in ['no', 'n']:
            return
        elif user_decision not in ['yes', 'y']:
            print('Vui lòng nhập "yes" hoặc "no".')

if __name__ == "__main__":
    main()
