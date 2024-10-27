import sqlite3


conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
)
''')

cursor.executemany('''
    INSERT INTO countries (title) VALUES (?, ?)
''' [('Kyrgyzstan',), ('Germany',), ('China',)])


cursor.execute('''
CREATE TABLE IF NOT EXISTS schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    FOREIGN KEY (country_id) REFERENCES countries(id),
)
''')

cursor.executemany('''
INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)

    ('Bishkek', 127.0 1),
    ('Osh', 182.0, 1)
    ('Berlin', 891.7, 2),
    ('Munhen', 310.7, 2),
    ('Pekin', 16410.5, 3),
    ('Shanghai', 6340.5, 3),
    ('Guangzhou', 7434.4, 3)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id),
)
''')

cursor.executemany('''
INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)
    ('Aybek', 'Abdyrahmanov', 1),
    ('Medet', 'Musaev', 1),
    ('Nursultan', 'Kadyrov', 2),
    ('Bermet', 'Kubanychbekov', 2),
    ('Nazira', 'Tairova', 2)
    
''')


conn.commit()

def show_students_by_city():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()


    cursor.execute('''
    SELECT id, title from cities
        
    ''')
    cities = cursor.fetchall()

    print("You can display a list of students by selected city id from those listed")
    for city in cities:
        print(f'{city[0]}: {city[1]}')


    while True:
     try:
         city_id = int(input('Enter a city id: '))
         if city_id == 0:
             print('Exit the programm!')
             break

         cursor.execute('''
         SELECT students.first_name, students.last_name, countries.title, cities.city_id
         FROM students,
         JOIN cities ON students.city_id = cities.id
         JOIN countries ON cities.country_id = countries.id
         WHERE cities.id = ?
         
         ''', (city_id,))

         students = cursor.fetchall()
         if students:
             print(f'\n Students in city {city_id}:')
             for student in students:
                 print(f'Name: {student[0]}: Last_name: {student[1]}, Country: {student[2]}, City: {student[3]}')
         else:
             print('Dont\'t have students in this city.')
     except ValueError:
         print('Enter a valid numeric id value.')
     except Exception as e:
         print('Error:', e)

     conn.close()


