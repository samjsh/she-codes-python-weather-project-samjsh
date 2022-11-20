import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    # strftime = format
    format = date.strftime ("%A %d %B %Y")
    return format

    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    # pass


def convert_f_to_c(temp_in_farenheit):
    celsius = (float(temp_in_farenheit) - 32) * (5 / 9)
    return (round(celsius, 1))
    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
    # pass


def calculate_mean(weather_data):
    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    # pass
    weather_data = list(map(float, weather_data)) #convert elements in weather data to list and in float type
    avg = sum(weather_data) / len(weather_data)
    return float(avg)


def load_data_from_csv(csv_file_location):
    weather = [] #creating empty list
    with open (csv_file_location) as csv_file: #opening csv file
        reader = csv.reader(csv_file) #reading
        next (reader) #skipping headers
        for line in reader: #for loop for each row in csv
            if len(line) > 0: #if the row is not empty
                weather.append([line[0], int(line[1]), int(line[2])]) #run the following. Appending data from empty row to list. A list within a list. Turned some strings into integers and making sure we are returning the right type of data
    return weather #return the list


def find_min(weather_data):
    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """
    # pass
    if len(weather_data) == 0:
        return ()
    list = weather_data
    index = 0
    min_number = min(weather_data)
    last_index = 0
    for num in list:
        print(num)
        print(index)
        #check if num equals min number
        if num == min_number:
            last_index = index
        
        index = index+1
    return (float(min_number), last_index)
    # """Calculates the minimum value in a list of numbers.


def find_max(weather_data):
    if len(weather_data) == 0:
        return ()
    list = weather_data
    index = 0
    max_number = max(weather_data)
    last_index = 0
    for num in list:
        print(num)
        print(index)

        if num == max_number:
            last_index = index
        index = index+1
    return (float(max_number), last_index)
    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """
    # pass 

def generate_summary(weather_data):
    min_temp = []
    max_temp = []
    date = []

    for item in weather_data:
        min_temp.append(convert_f_to_c(item[1]))
        max_temp.append(convert_f_to_c(item[2]))
        date.append(convert_date(item[0]))
    
    #number of days overview
    number_of_days = len(weather_data)

    #overall low temp
    (overall_min_temp, overall_min_index) = find_min(min_temp) 
    
    #overall high temp
    (overall_max_temp, overall_max_index) = find_max(max_temp)

    #overall min date
    overall_min_date = date[overall_min_index]

    #overall max date
    overall_max_date = date[overall_max_index]

    #average min
    average_min_temp = calculate_mean(min_temp)
    formatted_min_temp = round(average_min_temp, 1)

    #average max
    average_max_temp = calculate_mean(max_temp)
    formatted_max_temp = round(average_max_temp, 1)

    summary = f"""{number_of_days} Day Overview
  The lowest temperature will be {overall_min_temp}°C, and will occur on {overall_min_date}.
  The highest temperature will be {overall_max_temp}°C, and will occur on {overall_max_date}.
  The average low this week is {formatted_min_temp}°C.
  The average high this week is {formatted_max_temp}°C.
"""
        
    return summary

    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    # pass
    ########################
# 8 Day Overview
#   The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is 11.4°C.
#   The average high this week is 18.8°C.

#     weather_data_celsius = convert_f_to_c(weather_data)
#     weather_data_celsius = (float(weather_data) - 32) * (5 / 9)
#     return (round(weather_data_celsius, 1))
#     overview = f"{len(weather_data)} Day Overview"
#     first_line = f"The lowest temperature will be {find_min(weather_data_celsius)}, and will occur on {convert_date(weather_data)} /n"
#     second_line = f"The highest temperature will be {find_max(weather_data_celsius)}, and will occur on {convert_date(weather_data)} /n"
#     third_line = f"The average low this week is "
# def generate_daily_summary(weather_data):
#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """



def generate_daily_summary(weather_data):
    data_to_return = ""
    for daily_weather_list in weather_data:
        # date_string = --somehow grab the date from the item
        date_string = daily_weather_list[0]
        converted_date_string = convert_date(date_string)
        min_temp_f = daily_weather_list[1]
        min_temp_c = convert_f_to_c(min_temp_f) #RE-USING "convert_f_to_c" function
        max_temp_f = daily_weather_list[2]
        max_temp_c = convert_f_to_c(max_temp_f) #RE-USING "convert_f_to_c" function
        day_summary = f"---- {converted_date_string} ----\n  Minimum Temperature: {min_temp_c}°C\n  Maximum Temperature: {max_temp_c}°C\n\n"
        data_to_return = data_to_return + day_summary
        
    print(data_to_return)
    return data_to_return
        # formatted_date = convert_date(date_string)
    # for item in weather_data:
    #     formatted_date = convert_date(item[0, 0])
    #     min_temp_c = convert_f_to_c(item[0, 1])
    #     formatted_min_temp = format_temperature(min_temp_c)
    #     max_temp_c = convert_f_to_c(item[2])
    #     formatted_max_temp = format_temperature(max_temp_c)
    #     daily_summary.append([formatted_date, formatted_min_temp, formatted_max_temp])
    # for individual_day in daily_summary:
    #     date = individual_day[0]
    #     individual_min = individual_day[1]
    #     individual_max = individual_day[2]
    #     summary = (f"---- {date} ----\n  Minimum Temperature: {individual_min}\n  Maximum Temperature: {individual_max}\n")
    # print(summary)
    # return summary