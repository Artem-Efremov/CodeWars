"""
Introduction
  	In the United Kingdom, the driving licence is the official document which authorises its holder to operate various types of motor vehicle on highways and some other roads to which the public have access. In England, Scotland and Wales they are administered by the Driver and Vehicle Licensing Agency (DVLA) and in Northern Ireland by the Driver & Vehicle Agency (DVA). A driving licence is required in the UK by any person driving a vehicle on any highway or other road defined in s.192 Road Traffic Act 1988[1] irrespective of ownership of the land over which the road passes, thus including many which allow the public to pass over private land; similar requirements apply in Northern Ireland under the Road Traffic (Northern Ireland) Order 1981. (Source Wikipedia)
 
Driving
Task
  	The UK driving number is made up from the personal details of the driver. The individual letters and digits can be code using the below information
 
Rules
  	1–5: The first five characters of the surname (padded with 9s if less than 5 characters)

6: The decade digit from the year of birth (e.g. for 1987 it would be 8)

7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)

9–10: The date within the month of birth

11: The year digit from the year of birth (e.g. for 1987 it would be 7)

12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name

14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9

15–16: Two computer check digits. We will always use "AA"
 

Your task is to code a UK driving license number using an Array of data. The Array will look like

data = ["John","James","Smith","01-Jan-2000","M"]

Where the elements are as follows
  	0 = Forename

1 = Middle Name (if any)

2 = Surname

3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)

4 = M-Male or F-Female
 

You will need to output the full 16 digit driving license number.

Good luck and enjoy!

"""





def driver(data):
    # 1. Case insensitive
    data = [i.upper() for i in data]
    
    # 2. Initialization
    name = data[0]
    mid_name = data[1]
    surname = data[2]
    birth_date = data[3].split('-') 
    sex = data[4]
    
    birth_day = birth_date[0]
    birth_month = birth_date[1][:3]
    birth_year = birth_date[2]
    
    # 3. Additional info
    months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 
              'APR': 4, 'MAY': 5, 'JUN': 6, 
              'JUL': 7, 'AUG': 8, 'SEP': 9, 
              'OCT': 10, 'NOV': 11, 'DEC': 12}
              
    incr_sex = {'M': 0, 'F': 50}
    
    # 4. Preparation of elements
    chr_1_5 = (surname + '9' * 5)[:5]
    chr_6 = birth_year[-2]
    chr_7_8 = str(months[birth_month] + incr_sex[sex]).zfill(2)
    chr_9_10 = birth_day.zfill(2)
    chr_11 = birth_year[-1]
    chr_12_13 = (name[:1] + mid_name[:1] + '9' * 2)[:2]
    chr_14 = '9'
    chr_15_16 = "AA"
    
    # 5. Join
    uk_driving_number = (chr_1_5 + chr_6 + chr_7_8 + chr_9_10 +
                         chr_11 + chr_12_13 + chr_14 + chr_15_16)
                         
    return uk_driving_number











test.describe("Random tests")
import random

def driver2(data):
    months = {"Jan": ("01", "51"), "Feb": ("02", "52"), "Mar": ("03", "53"), "Apr": ("04", "54"), "May": ("05", "55"), "Jun": ("06", "56"), "Jul": ("07", "57"), "Aug": ("08", "58"), "Sep": ("09", "59"), "Oct": ("10", "60"), "Nov": ("11", "61"), "Dec": ("12", "62")}
    forename, middle_name, surname, date_of_birth, m_or_f = data
    surname_first_five = (surname.upper() + "9999")[:5]
    decade_digit, year_digit = date_of_birth[-2], date_of_birth[-1]
    birth_month, birth_day = months[date_of_birth[3:6]][m_or_f == "F"], date_of_birth[0:2]
    initials = forename[0] + (middle_name[0] if middle_name else "9")

    return "{}{}{}{}{}{}9AA".format(surname_first_five, decade_digit, birth_month, birth_day, year_digit, initials)
    
names = ["Eugene", "Kade", "Johanna", "Andrew", "Maddison", "Marin", "Wayne", "Nick", "Mccullough", "Sandoval", "Hurst", "Gibbs", "Benson", "Holland", "Crane", "Lee", "Wilson", "Clara", "Zhang", "Cummings", "Richmond", "Kadyn", "Stevens", "Laila", "Alan", "Angel", "Yadiel", "Saul", "Jovan", "Faith", "King", "Milagros", "Scott", "Brennan", "Ashanti", "Dayton", "Lindsey", "Gilbert", "Jamya", "Sam", "Madeleine", "Levine", "Luna", "Addison", "Bethany", "Zoie", "Landyn", "Mireya", "Mcgee", "Kirk", "Kirsten", "Kamren", "Vega", "Stephany", "Brooks", "Issac", "Hays", "Jasmin", "Benitez", "Alfonso", "Shepherd", "Jenkins"]

for rtest in range(100):
  day = random.randint(10, 28)
  month = random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
  year = random.randint(1930, 2000)
  d = "{}-{}-{}".format(day, month, year)
  g = random.choice(["M", "F"])

  data = [random.choice(names), random.choice(names), random.choice(names), d, g]
  solution = driver2(data)

  test.it("should work for random tests")
  test.assert_equals(driver(data), solution)
