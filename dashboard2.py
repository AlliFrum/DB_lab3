import cx_Oracle
import chart_studio
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as py
import re
import chart_studio.dashboard_objs as dash
chart_studio.tools.set_credentials_file(username='a.frumovych', api_key='GxqJZQysYWqzouu9uiwG')


def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return raw_fileId.replace('/', ':')


username = 'MYONLINEEDU'
password = 'RV-81-19-14f'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

#First query
castles1 = []
values1 = []
query1 = """
SELECT CASTLE_NAME, SUM(GOLD) AS TOTAL_GOLD
FROM HEROES
GROUP BY CASTLE_NAME
ORDER BY TOTAL_GOLD ASC
"""
cursor.execute(query1)

for row in cursor.fetchall():
    castles1.append(row[0])
    values1.append(row[1])
bar = go.Bar(x=castles1, y=values1)
bar = py.plot([bar], auto_open=True, file_name="Plot3_1")



#Second query
castles2 = []
values2 = []
query2 = '''
SELECT CASTLE_NAME, round ((SUM(GOLD) + 0.0) / tg.TOTAL * 100, 2) AS PERCENT_
FROM 
(
    SELECT SUM(GOLD) AS TOTAL
    FROM HEROES
)tg, HEROES
GROUP BY CASTLE_NAME, tg.TOTAL
ORDER BY PERCENT_ ASC
'''

cursor.execute(query2)


for row in cursor.fetchall():
    castles2.append (row[0])
    values2.append(row[1])
pie = go.Pie (labels = castles2, values = values2)
pie = py.plot([pie],auto_open = True, file_name = "Plot3_2")


#Third query
level = []
attack = []
query3 = '''
SELECT UNIT_LEVEL, MAX(ATTACK) AS MAX_ATTACK
FROM HEROES
GROUP BY UNIT_LEVEL
ORDER BY UNIT_LEVEL
'''

cursor.execute(query3)

for row in cursor.fetchall():
    level.append (int(row[0]))
    attack.append(row[1])
scatter = go.Scatter (x = level, y = attack)
scatter = py.plot([scatter],auto_open = True, file_name = "Plot3_3")


my_dboard = dash.Dashboard()
bar_id = fileId_from_url(bar)
pie_id = fileId_from_url(pie)
scatter_id = fileId_from_url(scatter)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': 'Query 1'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': 'Query 2'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': 'Query 3'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dboard, 'Lab_3')

cursor.close()
connection.close()
