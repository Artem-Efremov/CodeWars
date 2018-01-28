"""
Introduction
    Drink driving is an issue all around the world! On average 3,000 people are killed or seriously injured each year in drink drive collisions, nearly one in six of all deaths on the road involve drivers who are over the legal alcohol limit. 

If you've been out drinking you may still be affected by alcohol the next day. You may feel OK, but you may still be unfit to drive or over the legal alcohol limit. It's impossible to get rid of alcohol any faster. A shower, a cup of coffee or other ways of 'sobering up' will not help. It just takes time.
 

Description
    Your task is to write a kata that will work out if you are safe to drive! You will be given some alcoholic drinks, a time when you stopped drinking and the time you would like to drive.
You will need to return the total units (to 2 decimal places) of the alcoholic drinks and a boolean value true if you are able to drive or false if you are still unable to drive.
Task
    Create a method called drive that takes an array of drinks in the format [[strength, volume]] a time when you finished drinking and a time when you would like to drive.
eg. drive([[10.0,100]], "20:00", "21:00") and it must return [1.0, false]
Rules
    1. On average it takes a person 1 hour for their body to remove 1 unit of alcohol.
2. Units of alcohol are calculated by strength (ABV) x volume (ml) / 1000 = units. More information can be found here
3. Data passed will be in the format ([[strength,volume]], finished, drive_time). Where finished is the time you stopped drinking and drive_time is the time you would like to drive.
4. If the finished >= drive_time then you can assume that it is the next day.
5. Times are passed as strings and are in 24 hour format.
6. Return total units to 2 decimal places rounded. For example 1.10 => 1.1 and 1.236 => 1.24
7. Return true if you are able to drive and false if you are not.
Example
alcohol = [[5.2,568],[5.2,568],[5.2,568],[12.0,175],[12.0,175],[12.0,175]]
drive(alcohol, "23:00", "08:15")
should return

[15.16, False]
Good luck and enjoy!

"""






def str_time_to_minutes(time):
    time_split = time.split(':')
    minutes = int(time_split[0]) * 60 + int(time_split[1])
    return minutes


def drive(drinks, finished, drive_time):
    units = 0
    for i in drinks:
        units += i[0] * i[1] / 1000
    units = round(units, 2)

    finished = str_time_to_minutes(finished)
    drive_time = str_time_to_minutes(drive_time)

    if drive_time <= finished:
        time = 1440 - finished + drive_time
    else:
        time = drive_time - finished
    time = time / 60
    able_to_drive = units / time < 1
    res = [units, able_to_drive]

    return res









def drive(drinks, finished, drive_time):
    alcohol = sum(strength * volume for strength, volume in drinks) / 1000
    minutes_passed = (
        int(drive_time[:2]) * 60 + int(drive_time[-2:]) -
        int(finished[:2]) * 60 - int(finished[-2:])) % (24 * 60)
    return [round(alcohol, 2), minutes_passed / 60 > alcohol]











# Test Cases:
import datetime
import random

def drive_tester(drinks, finished, drive_time):
    total_units = 0
    for drink in drinks:
        total_units += float(drink[0]) * drink[1] / 1000
    finished = datetime.datetime.strptime(finished.replace(":",""), "%H%M")
    drive_time = datetime.datetime.strptime(drive_time.replace(":",""), "%H%M")
    if finished > drive_time: drive_time = drive_time + datetime.timedelta(days=1)
    time_when_can_drive = finished + datetime.timedelta(hours=total_units)
    return [round(total_units,2), time_when_can_drive < drive_time]

for rtest in range(250):
    drinks_li = []
    for dr in range(random.randint(1,10)):
        drinks_li.append([round(random.uniform(5.0,25.0),2),random.randint(75,500)])
    ft = str(random.randint(10,23)) + ":" + str(random.randint(10,59))
    dt = str(random.randint(10,23)) + ":" + str(random.randint(10,59))

    solution = drive_tester(drinks_li,ft,dt)
    test.it("Should return '"+str(solution)+"'")
    test.assert_equals(drive(drinks_li,ft,dt), solution)