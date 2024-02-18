###################   DZ_9_01 ############################# вик. метод count()

# def popular_words(text, words):
#    # Разділяю текст і в нижній регістор його
#     word_list = text.lower().split()
#     # створюю словник зі значеннями
#     word_count = {word: word_list.count(word) for word in words}
#     return word_count
#
# # Перевірка функції
# assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


###################   DZ_9_02 #############################


def difference(*args): #### використовуємо аргумент, якщо не має - 0
    if not args:
        return 0
    else:
        return round(max(args) - min(args), 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
