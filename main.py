

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
    numbers_words = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five"
    }
    return numbers_words[number]


def show_result(word):
    print("Соответствующее слово:", word)


while True:
    number = get_number()
    result = correct_number(number)

    if result:
        word = get_word(number)
        show_result(word)
        break