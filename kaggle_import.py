import csv
import cx_Oracle


username = 'MYONLINEEDU'
password = 'RV-81-19-14f'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)

filename = "H3Units.csv"

 

with open(filename, newline='') as file:

    reader = csv.reader(file, delimiter = ',')
    next(reader, None) #Пропускаем заголовки
    unique_castles = []
    unique_units = []


    for row in reader:
        unit = row[0]
        Castle = row[1]
        level = row[2]
        attack = row[3]
        speed = row[8]
        gold = row[11]

        cursor = connection.cursor()
        if unit not in unique_units:
            unique_units.append(unit)
            first_query = "insert into unit(unit_name) values (:unit_name)"
            cursor.execute(first_query, unit_name = unit)
        if Castle not in unique_castles:
            unique_castles.append(Castle)
            second_query = "insert into castle(castle_name) values (:castle_name)"
            cursor.execute(second_query, castle_name = Castle)
        third_query = "insert into unit_castle(unit_name, castle_name) values (:unit_name, :castle_name)"
        cursor.execute(third_query, unit_name = unit, castle_name = Castle)
        if level[-1] == '+' or level[-1] == '*':
            level = level[0] + '.5'
        fourth_query = "insert into unit_level(unit_name, unit_level) values (:unit_name, :unit_level)"
        cursor.execute(fourth_query, unit_name = unit, unit_level = level)
        fifth_query = "insert into unit_info(unit_name, gold, speed, attack) values (:unit_name, :gold, :speed, :attack)"
        cursor.execute(fifth_query, unit_name = unit, gold = gold, speed = speed, attack = attack)
    
    cursor.close()
    file.close()
    connection.commit()
