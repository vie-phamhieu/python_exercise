# Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
def check_input_number():
    while True:
        try:
            number = float(input('Nhập vào số thực cần kiểm tra: '))
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

def is_integer(num):
    """Check whether a given number is an integer or not."""
    return num.is_integer()

if __name__ == '__main__':
    while True:
        num = check_input_number()
        print('\nSố đang kiểm tra: ', num)
        if is_integer(num):
            print('Đây là một số nguyên.')
        else:
            print('Đây không phải là một số nguyên.')
        if not check_user_want_to_continue_or_not():
            break
