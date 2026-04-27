

def get_number():
    while True:
        try:
            number = int(input("Введите число от 1 до 5: "))
            return number
        except ValueError:
            print("Ошибка: нужно ввести число.")


def correct_number(number):
    if 1 <= number <= 5:
        return True
    else:
        print("Ошибка: число должно быть от 1 до 5.")
        return False


def get_word(number):
    if number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"


def show_result(word):
    print("Соответствующее слово:", word)


while True:
    number = get_number()
    result = correct_number(number)

    if result:
        word = get_word(number)
        show_result(word)
        break