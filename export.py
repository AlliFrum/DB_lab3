import csv
import cx_Oracle


username = 'MYONLINEEDU'
password = 'RV-81-19-14f'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)

cursor_unit = connection.cursor()
cursor_castle = connection.cursor()
cursor_unit_castle = connection.cursor()
cursor_unit_info = connection.cursor()
cursor_unit_level = connection.cursor()


cursor_unit.execute("""SELECT TRIM(unit_name) FROM UNIT""")
cursor_castle.execute("""SELECT TRIM(castle_name) FROM CASTLE""")
cursor_unit_castle.execute("""SELECT TRIM(unit_name), TRIM(castle_name) FROM UNIT_CASTLE""")
cursor_unit_info.execute("""SELECT TRIM(unit_name), gold, speed, attack FROM UNIT_INFO""")
cursor_unit_level.execute("""SELECT TRIM(unit_name), TRIM(unit_level) FROM UNIT_LEVEL""")

with open("unit.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        for row in cursor_unit:
            writer.writerow(row)
file.close()

with open("castle.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        for row in cursor_castle:
            writer.writerow(row)
file.close()

with open("unit_castle.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        for unit_name, castle_name in cursor_unit_castle:
            writer.writerow([unit_name, castle_name])
file.close()

with open("unit_info.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        for unit_name, gold, speed, attack in cursor_unit_info:
            writer.writerow([unit_name, gold, speed, attack])
file.close()

with open("unit_level.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        for unit_name, unit_level in cursor_unit_level:
            writer.writerow([unit_name, unit_level])
file.close()

cursor_unit.close()
cursor_castle.close()
cursor_unit_castle.close()
cursor_unit_info.close()
cursor_unit_level.close()
