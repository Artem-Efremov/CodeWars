
"""
You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

Each part of the string is of the form: h|m|s where h, m, s are positive or null integer (represented as strings) with one or two digits. There are no traps in this format.

To compare the results of the teams you are asked for giving three statistics; range, average and median.

Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

Mean or Average : To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.

Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

Your task is to return a string giving these 3 values. For the example given above, the string result will be

"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

of the form:

"Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"

where hh, mm, ss are integers (represented by strings) with each 2 digits.

Remarks:

    if a result in seconds is ab.xy... it will be given truncated as ab.

    if the given string is "" you will return ""



"""











def stat(strg):
    

    def time_dec(mas):
        """ Convert list of int numbers '[hh, mm, ss]' to time in seconds"""
        return mas[0] * 3600 + mas[1] * 60 + mas[2]

    def time_enc(time):
        """ Convert time in seconds to string 'hh|mm|ss' """
        hh = str(time // 3600)
        mm = str((time % 3600) // 60)
        ss = str((time % 3600) % 60)
        return '|'.join([i.zfill(2) for i in [hh, mm, ss]])

    def time_range(mas):
        return time_enc(time_dec(mas[-1]) - time_dec(mas[0]))

    def time_average(mas):
        return time_enc(sum([time_dec(i) for i in mas]) // len(mas))
    
    def time_median(mas):
        lenght = len(mas)
        return time_average( [mas[lenght//2]]  
                             if lenght % 2 else 
                             [mas[(lenght//2)-1], mas[lenght//2]])   


    if strg:
        res = sorted([list(map(int, i.split('|'))) for i in strg.split(', ')])
        return "Range: {0} Average: {1} Median: {2}".format(time_range(res), time_average(res), time_median(res))
    return strg
    
    
    
    
    
    
    
    
    
    
    
    

def stat(strg):
    
    def get_time(string):
        """ Convert string 'hh|mm|ss' to time in seconds """
        mas = list(map(int, string.split('|'))))
        return mas[0] * 3600 + mas[1] * 60 + mas[2]

    def get_format(time):
        """ Convert time in seconds to string 'hh|mm|ss' """
        hh = str(time // 3600)
        mm = str((time % 3600) // 60)
        ss = str((time % 3600) % 60)
        return '|'.join([i.zfill(2) for i in [hh, mm, ss]])

    def get_range(mas):
        return get_format(mas[-1] - mas[0])

    def get_average(mas):
        return get_format(sum(mas) // len(mas))
    
    def get_median(mas):
        mid = len(mas) >> 1
        return get_average( [ mas[mid] ] if len(mas) % 2 else 
                             [ mas[mid-1], mas[mid] ] )   

    if strg:
        res = sorted(list(map(get_time, string.split(', '))))
        return "Range: {0} Average: {1} Median: {2}".format(get_range(res), get_average(res), get_median(res))
    return strg
    
    
    

    
    
    
    
    
    
    
 
# TESTS



print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"), 
    "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34")
print(stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"), 
    "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00")
print(stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|32|34, 2|17|17"), 
    "Range: 00|31|17 Average: 02|27|10 Median: 02|24|57")
print(stat("0|15|59, 0|16|16, 0|17|20, 0|22|34, 0|19|34, 0|15|0"), 
    "Range: 00|07|34 Average: 00|17|47 Median: 00|16|48")
print(stat("11|15|59, 10|16|16, 12|17|20, 9|22|34, 13|19|34, 11|15|17, 11|22|00, 10|26|37, 12|17|48, 9|16|30, 12|20|14, 11|25|11"), 
    "Range: 04|03|04 Average: 11|14|36 Median: 11|18|59")
print(stat("1|15|59, 1|16|16, 1|17|20, 1|22|34, 1|19|34, 1|15|17, 1|22|00, 1|26|37, 1|17|48, 1|16|30, 1|20|14, 1|25|11"), 
    "Range: 00|11|20 Average: 01|19|36 Median: 01|18|41")
print(stat(""), "")
