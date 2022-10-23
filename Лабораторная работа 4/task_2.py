def get_count_char(str_):
    str_ = str_.lower()
    text = "".join(str_.split())
    letter_str = []
    for i in text:
        if i.isalpha():
            letter_str.append(i)

    letter_dict = {}
    DEFAULT_COUNT = 0
    for letter in letter_str:
        letter_dict[letter] = letter_dict.get(letter, DEFAULT_COUNT) + 1

    return letter_dict


def second_func(dict_):
    sum_ = 0
    for letter in dict_:
        sum_ += dict_.get(letter)
    for letter in dict_:
        dict_[letter] = dict_.get(letter) / sum_ * 100
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(second_func(get_count_char(main_str)))