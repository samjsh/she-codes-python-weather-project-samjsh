import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    format = date.strftime ("%A %d %B %Y")
    return format


def convert_f_to_c(temp_in_farenheit):
    celsius = (float(temp_in_farenheit) - 32) * (5 / 9)
    return (round(celsius, 1))


def calculate_mean(weather_data):
    weather_data = list(map(float, weather_data))
    avg = sum(weather_data) / len(weather_data)
    return float(avg)


def load_data_from_csv(csv_file_location):
    weather = []
    with open (csv_file_location) as csv_file:
        reader = csv.reader(csv_file)
        next (reader)
        for line in reader:
            if len(line) > 0:
                weather.append([line[0], int(line[1]), int(line[2])])
    return weather


def find_min(weather_data):
    if len(weather_data) == 0:
        return ()
    list = weather_data
    index = 0
    min_number = min(weather_data)
    last_index = 0
    for num in list:
        if num == min_number:
            last_index = index
        
        index = index+1
    return (float(min_number), last_index)


def find_max(weather_data):
    if len(weather_data) == 0:
        return ()
    list = weather_data
    index = 0
    max_number = max(weather_data)
    last_index = 0
    for num in list:
        if num == max_number:
            last_index = index
        index = index+1
    return (float(max_number), last_index)


def generate_summary(weather_data):
    min_temp = []
    max_temp = []
    date = []

    for item in weather_data:
        min_temp.append(convert_f_to_c(item[1]))
        max_temp.append(convert_f_to_c(item[2]))
        date.append(convert_date(item[0]))
    
    number_of_days = len(weather_data)

    (overall_min_temp, overall_min_index) = find_min(min_temp) 
    (overall_max_temp, overall_max_index) = find_max(max_temp)
    overall_min_date = date[overall_min_index]
    overall_max_date = date[overall_max_index]
    average_min_temp = calculate_mean(min_temp)
    formatted_min_temp = round(average_min_temp, 1)
    average_max_temp = calculate_mean(max_temp)
    formatted_max_temp = round(average_max_temp, 1)

    summary = f"""{number_of_days} Day Overview
  The lowest temperature will be {overall_min_temp}°C, and will occur on {overall_min_date}.
  The highest temperature will be {overall_max_temp}°C, and will occur on {overall_max_date}.
  The average low this week is {formatted_min_temp}°C.
  The average high this week is {formatted_max_temp}°C.
"""
    return summary



def generate_daily_summary(weather_data):
    data_to_return = ""
    for daily_weather_list in weather_data:
        date_string = daily_weather_list[0]
        converted_date_string = convert_date(date_string)
        min_temp_f = daily_weather_list[1]
        min_temp_c = convert_f_to_c(min_temp_f)
        max_temp_f = daily_weather_list[2]
        max_temp_c = convert_f_to_c(max_temp_f)
        day_summary = f"---- {converted_date_string} ----\n  Minimum Temperature: {min_temp_c}°C\n  Maximum Temperature: {max_temp_c}°C\n\n"
        data_to_return = data_to_return + day_summary
        
    return data_to_return