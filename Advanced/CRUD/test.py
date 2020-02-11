import datetime

#mysql_time = 'Tue Apr 26 03:10:02'

mysql_time = '2020-02-11 00:00:00'

print(datetime.datetime.strptime(str(mysql_time), '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d %H:%M:%S"))