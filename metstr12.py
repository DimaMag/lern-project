# Строки - Методы строк


# len() - метод для подсчета количества символов в строке
# upper() - метод для преобразования строки в верхний регистр
# lower() - метод для преобразования строки в нижний регистр
# capitalize() - метод для преобразования первого символа строки в верхний регистр
# title() - метод для преобразования первого символа каждого слова строки в верхний регистр
# startswith() - метод для проверки начала строки
# endswith() - метод для проверки конца строки
# find() - метод для поиска подстроки в строке, если подстрока не найдена возвращает -1
# rfind() - метод для поиска подстроки в обратном порядке, если подстрока не найдена возвращает -1
# index() - метод для поиска подстроки в строке, если подстрока не найдена возвращает исключение
# rindex() - метод для поиска подстроки в обратном порядке, если подстрока не найдена возвращает исключение
# split() - метод для разделения строки на подстроки
# join() - метод для объединения подстрок в строку
# replace() - метод для замены подстроки в строке
# isdigit() - метод для проверки, является ли строка числом
# isalpha() - метод для проверки, является ли строка буквами
# isalnum() - метод для проверки, является ли строка буквами и цифрами
# islower() - метод для проверки, является ли строка маленькими буквами
# isupper() - метод для проверки, является ли строка большими буквами


#test_string_1 = "Hello, World!"
#test_string_2 = "1234567890"


#print("\nДлина строки\n" + "-" * 50)
#print(len(test_string_1))
#print(len(test_string_2))


#print("\nИзменение регистра\n" + "-" * 50)
#print(test_string_1.upper())
#print(test_string_1.lower())
#print(test_string_1.capitalize())
#print(test_string_1.title())


#print("\nstartswith, endswith\n" + "-" * 50)
#print(test_string_1.startswith("World"))
#print(test_string_1.endswith("rld!"))
#
#
#print("\nПоиск подстрок\n" + "-" * 50)
#print(test_string_1.find("H"))
#print(test_string_1.rfind("q"))
#print(test_string_1.index("l"))
#print(test_string_1.rindex("d"))


#print("\nСтроки и списки\n" + "-" * 50)
#print(test_string_1.split(", "))
#print(", ".join(["Hello", "World!"]))
#
#
#print("\nЗамена подстрок\n" + "-" * 50)
#print(test_string_1.replace("World", "Universe"))
#
#
#print("\nПроверка содержания строки\n" + "-" * 50)
#print(test_string_1.isdigit())
#print(test_string_2.isdigit())
#print(test_string_1.isalpha())
#print(test_string_1.isalnum())
#print(test_string_1.islower())
#print(test_string_1.isupper())


#print("\nФорматирование строк совместно с использованием методов строк\n" + "-" * 50)
#products = ["Молоко", "Сыр", "Мясо"]
#print(*products, sep=' + ', end=' = ')
#print("100")
#print(" + ".join(products) + " = 100")
#print(f'{" + ".join(products)} = 100')

#print("   Hello, World!   ")


test_string_1 = "World is great!"
test_string_2 = "24856719"

print(len(test_string_1))
print(len(test_string_2))

print(test_string_1.upper())
print(test_string_1.lower())
print(test_string_1.capitalize())
print(test_string_1.title())

print(test_string_1.startswith("great"))
print(test_string_1.endswith("eat!"))

print(test_string_1.find("W"))
print(test_string_1.rfind("g"))
print(test_string_1.index("l"))
print(test_string_1.rindex("s"))

print(test_string_1.split(", "))
print(", ".join(["World", "is great!"]))

print(test_string_1.replace("great", "super"))


print(test_string_1.isdigit())
print(test_string_2.isdigit())
print(test_string_1.isalpha())
print(test_string_1.isalnum())
print(test_string_1.islower())
print(test_string_1.isupper())


