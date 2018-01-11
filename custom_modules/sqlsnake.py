#!/usr/bin/python3
import os,sys,mysql.connector

# connects to database to use cursor in functions
config = {   'user' : 'FlyingToastersUn',
            'password' : 'LensWipeConcreteVagabond',
            'host' :'FlyingToastersUnlimited.mysql.pythonanywhere-services.com',
            'database': 'FlyingToastersUn$gbox' }
def get_db():
    try:
        connection = mysql.connector.connect(**config)

        #
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        connection.close()
    return connection


#Logs the data from growbox
def log_data(ptime,t,h,l,f):
    insert = ("INSERT INTO readings(post_time, temp,hum,light_on,fan_on) VALUES(%s,%s,%s,%s,%s)")
    box_readings = (ptime,t,h,l,f)
    logcon = get_db()
    logcursor  = logcon.cursor()
    logcursor.execute(insert,box_readings)
    logcon.commit()
    logcursor.close()
    logcon.close()
# gets the current power states for the box
def get_power_states():
    states = ("SELECT light_on, fan_on FROM readings ORDER BY id DESC;")
    stcon = get_db()
    stcursor = stcon.cursor()
    stcursor.execute(states)
    stdata = stcursor.fetchall()
    stcursor.close()
    stcon.close()
    return stdata

# Gets the most current reading
def current_data():
    latest  = ("SELECT temp,hum FROM readings ORDER BY post_time DESC LIMIT 1;")
    latcon = get_db()
    latcursor  = latcon.cursor()
    latcursor.execute(latest)
    latdata  = latcursor.fetchone()
    latcursor.close()
    latcon.close()
    return latdata
#Returns all data
def get_all():
    readings  = ("SELECT * FROM readings;")
    rdcon = get_db()
    rdcursor  = rdcon.cursor()
    rdcursor.execute(readings)
    rddata  = cursor.fetchall()
    rdcursor.close()
    rdcon.close()
    return rddata
#returns hourly readings from readings
def get_last_day():
    hours = ("SELECT MIN(post_time), temp, hum FROM readings GROUP BY DATE(post_time), HOUR(post_time) ORDER BY post_time DESC LIMIT 24;")
    hrcon = get_db()
    hrcursor  = hrcon.cursor()
    hrcursor.execute(hours)
    hrdata  = hrcursor.fetchall()
    hrcursor.close()
    hrcon.close()
    return hrdata