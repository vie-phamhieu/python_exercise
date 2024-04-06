# Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
def get_input_number():
    while True:
        try:
            number = float(input('Nhập vào số cần tính: '))
            return number
        except ValueError as ve:
            print(f'Cần nhập số nguyên. Vui lòng nhập lại.\nMã lỗi: {ve}')


def calculate_result(number):
    return number * 3 + 1


def main():
    while True:
        num = get_input_number()
        result = calculate_result(num)
        print('Kết quả là:', result)

        while True:
            user_decision = input('Bạn có muốn tiếp tục tính không? Yes/No: ').lower()
            if user_decision in ['yes', 'y']:
                break
            elif user_decision in ['no', 'n']:
                return
            else:
                print("Vui lòng nhập lại!")


if __name__ == '__main__':
    main()
