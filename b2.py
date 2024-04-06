# Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
def check_number():
    while True:
        try:
            numbers = float(input('Nhập số cần tính: '))
            return numbers
        except ValueError:
            print('Bạn cần nhập số nguyên, vui lòng nhập lại.')

def calculator(numbers):
    return  numbers**2 / 3

def main():
    while True:
        number = check_number()
        result = calculator(number)
        print('Kết quả là: ',result)
        while True:
            user_decision = input('Bạn có muốn tiếp tục tính không? (Yes/No)').lower()
            if user_decision in ('yes', 'y'):
                break
            elif user_decision in ('no', 'n'):
                return
            else:
                print('Vui lòng chọn Yes/No')

if __name__ == "__main__":
    main()