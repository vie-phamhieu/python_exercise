# Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
'''
Cách giải:
- Số chính nguyên là số mà căn bậc 2 của nó là một số nguyên. Ví dụ, 4 =  2 * 2; 9 =  3 * 3; 16 = 4 * 4.

'''
import math

def check_input_number():
    try:
        number = input('Nhập vào số nguyên cần kiểm tra (nhấn Enter để dừng): ')
        if number.strip() == "":
            return None  # Trả về None nếu người dùng không nhập gì
        else:
            return int(number)
    except ValueError:
        print('Nhập sai. Vui lòng nhập số nguyên.')

def is_perfect_square(num):
    if num is None:
        return False
    return math.isqrt(num) ** 2 == num

def main():
    print('Nhấn Enter để dừng chương trình')
    while True:
        num = check_input_number()
        if num is None:
            print("Dừng chương trình.")
            break
        result = is_perfect_square(num)
        if result:
            print(f'Số {num} là số chính phương')
        else:
            print(f'Số {num} không phải là số chính phương')

if __name__ == '__main__':
    main()
