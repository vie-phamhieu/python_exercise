# Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False

def check_numbers():
    while True:
        try:
            numbers = int(input('Nhập vào số nguyên cần kiểm tra: '))
            return numbers
        except ValueError:
            print('Nhập sai. Vui lòng nhập số nguyên')

def calculator(num):
    if num  % 2 == 0:
        return 'chia hết' # Thay kết là return True để in ra là chia hết
    else:
        return 'không chia hết'
    
def main():
    while True:
        num = check_numbers()
        result = calculator(num)
        print(f'Số {num} là số {result} cho 2')
        while True:
            user_decision = input('Bạn có muốn tiếp tục kiểm tra hay không? y/n: ').lower()
            if user_decision in ['yes', 'y']:
                break
            elif user_decision in ['no', 'n']:
                return
            else: print('Vui lòng nhập y/n')

if __name__ == '__main__':
    main()