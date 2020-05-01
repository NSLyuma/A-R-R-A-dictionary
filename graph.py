from tkinter import *
from tkinter import ttk
import shelve

# Открываем словари
ar=shelve.open('ar_words.txt')
ra=shelve.open('ra_words.txt')

# -------------------Блок функций-------------------

# Функция для перевода слов
def translate():
    user_word=rus_word_tr.get()
    if user_word in ra:
        adi_tr.config(text=ra[user_word], fg='blue')
    rus_word_tr.delete(0, 'end')

    if user_word not in ra:
        adi_tr.config(text='')

    user_word=adi_word_tr.get()
    if user_word in ar:
        rus_tr.config(text=ar[user_word], fg='blue')
    adi_word_tr.delete(0, 'end')

    if user_word not in ar:
        rus_tr.config(text='')

# Функции для добавления новых слов
def add_both_word():
    new_word_rus=rus_word_ad.get()
    new_word_adi=adi_word_ad.get()
    ra[new_word_rus]=new_word_adi
    ar[new_word_adi]=new_word_rus
    ra.update()
    ar.update()
    rus_word_ad.delete(0, 'end')
    adi_word_ad.delete(0, 'end')

def add_in_rus():
    new_word_rus=rus_word_ad.get()
    new_word_adi=adi_word_ad.get()
    ra[new_word_rus]=new_word_adi
    ra.update()
    rus_word_ad.delete(0, 'end')
    adi_word_ad.delete(0, 'end')

def add_in_adi():
    new_word_adi=adi_word_ad.get()
    new_word_rus=rus_word_ad.get()
    ar[new_word_adi]=new_word_rus
    ar.update()
    rus_word_ad.delete(0, 'end')
    adi_word_ad.delete(0, 'end')

# -------------------Конец блока функций-------------------

# -------------------Блок графического интерфейса-------------------

# Создаём окно
window=Tk()
window.title('Russian-Adifiro/Adifiro-Russian translator')
# Настройка размеров окна приложения
window.geometry('400x300')

# Раздел вкладок
pages_control=ttk.Notebook(window)
translator_page=ttk.Frame(pages_control)
adi_rus_page=ttk.Frame(pages_control)
rus_adi_page=ttk.Frame(pages_control)
pages_control.add(translator_page, text='Translator')
pages_control.add(adi_rus_page, text='A-R dict')
pages_control.add(rus_adi_page, text='R-A dict')
pages_control.pack(expand=1, fill='both')

# Раздел перевода слов
# Название
title1=Label(translator_page, text='Translator')
title1.place(x=200, y=10, anchor=CENTER)
# Названия полей для ввода слов
enter_rus=Label(translator_page, text='Enter a russian word')
enter_adi=Label(translator_page, text='Enter an Adifiro word')
enter_rus.place(x=70, y=40, anchor=CENTER)
enter_adi.place(x=330, y=40, anchor=CENTER)
# Поля для ввода текста
rus_word_tr=Entry(translator_page)
adi_word_tr=Entry(translator_page)
rus_word_tr.place(x=70, y=60, anchor=CENTER)
adi_word_tr.place(x=330, y=60, anchor=CENTER)
# Кнопка для перевода слов
translate_button=Button(translator_page, text='Translate', command=translate)
translate_button.place(x=200, y=60, anchor=CENTER)
# Поля для вывода перевода слов
rus_tr=Label(translator_page, text='Russian translation', fg='grey')
adi_tr=Label(translator_page, text='Adifiro translation', fg='grey')
rus_tr.place(x=70, y=80, anchor=CENTER)
adi_tr.place(x=330, y=80, anchor=CENTER)

# Раздел добавления слов
# Название
title2=Label(translator_page, text='Add new words')
title2.place(x=200, y=120, anchor=CENTER)
# Примечание
note=Label(translator_page, text='Note: If you want to add one russian word with several Adifiro meanings,\npress \'Add in russian\'. Otherwise press \'Add in Adifiro\'.', fg='brown')
note.place(x=0, y=150, anchor=W)
# Названия полей для ввода слов
add_rus=Label(translator_page, text='Enter a russian word')
add_adi=Label(translator_page, text='Enter an Adifiro word')
add_rus.place(x=70, y=180, anchor=CENTER)
add_adi.place(x=330, y=180, anchor=CENTER)
# Поля для ввода текста
rus_word_ad=Entry(translator_page)
adi_word_ad=Entry(translator_page)
rus_word_ad.place(x=70, y=200, anchor=CENTER)
adi_word_ad.place(x=330, y=200, anchor=CENTER)
# Кнопки для добавления новых слов
add_both_button=Button(translator_page, text='Add both', command=add_both_word)
add_in_rus_button=Button(translator_page, text='Add in russian', command=add_in_rus)
add_in_adi_button=Button(translator_page, text='Add in Adifiro', command=add_in_adi)
add_both_button.place(x=200, y=200, anchor=CENTER)
add_in_rus_button.place(x=70, y=230, anchor=CENTER)
add_in_adi_button.place(x=330, y=230, anchor=CENTER)

# Вкладки со словарями
# Адифиро-русский словарь
ar_scr=Scrollbar(adi_rus_page)
ar_scr.pack(side=RIGHT, fill=Y)
adi_rus_dict=Listbox(adi_rus_page, width=200, height=400, yscrollcommand=ar_scr.set)
list_ar=list(ar.keys())
list_ar.sort()
for i in list_ar:
    adi_rus_dict.insert(END, i + ' - ' + ar[i])
    adi_rus_dict.pack()
# Русско-Адифиро словарь
ra_scr=Scrollbar(rus_adi_page)
ra_scr.pack(side=RIGHT, fill=Y)
rus_adi_dict=Listbox(rus_adi_page, width=200, height=400, yscrollcommand=ra_scr.set)
list_ra=list(ra.keys())
list_ra.sort()
for i in list_ra:
    rus_adi_dict.insert(END, i + ' - ' + ra[i])
    rus_adi_dict.pack()

# Смена иконки
window.iconbitmap('ar_ra.ico')

# Последняя строка вызывает функцию mainloop. Эта функция вызывает бесконечный цикл окна, поэтому окно будет ждать
# любого взаимодействия с пользователем, пока не будет закрыто
# В случае, если вы забудете вызвать функцию mainloop, для пользователя ничего не отобразится
window.mainloop()

# -------------------Конец блока графического интерфейса-------------------

# Закрываем словари
ra.close()
ar.close()

# Надо всё-таки додумать штуку, чтобы если слова нет в словаре, он НОРМАЛЬНО выводил Word not found.
# Как-то надо сделать, чтобы русский перевод стирался, когда вылезает Адифиро и наоборот.
# Сделать ярлык, чтобы открывать программу не отсюда. Чтобы это сделать, надо переделать py в exe.