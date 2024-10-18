volume = 1.44 * (2 ** 20)# перевод в байты
num_pages = 100
strings_on_page = 50
symbols_in_string = 25
count_symbols = (num_pages * strings_on_page * symbols_in_string) * 4
count_books = int(volume // count_symbols)
print("Количество книг, помещающихся на дискету:", count_books)
