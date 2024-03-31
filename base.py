import sqlite3

con = sqlite3.connect('data.db') #Подключение к таблице
cur = con.cursor()  #Создание курсора для работы с базой данных

                                                                                                          #+  -   -   -
cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, eat TEXT, cash TEXT, dyma TEXT)') # id,eat,cash,dyma
con.commit() # Утвердить в БД изменения
cur.execute("INSERT INTO  users(eat,cash,dyma) VALUES(?,?,?)", (1,2,3)) #Добавление записи в таблицу
con.commit() # id,eat,cash,dyma
for i in cur.execute(f'SELECT id,eat,cash,dyma FROM users'): #Получение всех значений из таблицы
    print(i)
cur.close() #Закрыть курсор
con.close() #Закрыть подключение к таблице
