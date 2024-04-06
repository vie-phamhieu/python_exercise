# Nhập vào nhiệt độ c, in ra nhiệt độ F
def get_input_temperature():
    while True:
        try:
            temperature = float(input('Vui lòng nhập nhiệt độ: '))
            return temperature
        except ValueError:
            print('Nhập sai nhiệt độ, vui lòng nhập một số.')


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def main():
    while True:
        celsius_temp = get_input_temperature()
        fahrenheit_temp = convert_celsius_to_fahrenheit(celsius_temp)
        print(f'Nhiệt độ được đổi sang độ F là: {fahrenheit_temp}')
        
        while True:
            user_decision = input('Bạn có muốn đổi nữa không? Yes/No: ').lower()
            if user_decision in ('yes', 'y'):
                break
            elif user_decision in ('no', 'n'):
                return
            else:
                print("Vui lòng nhập Y/N")


if __name__ == "__main__":
    main()
