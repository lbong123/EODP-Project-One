import json
import os
import re
import datetime
import csv
import matplotlib.pyplot as plt
   
def create_calendar(year_list):
    """ 
    Takes a non-unique list holding n years for n articles in the list

    """

    # make a unique set
    unique_years = set(year_list)
    year_counts = dict()

    # append to dictionary holding the year and counts
    for year in unique_years:
        year_counts[year] = year_list.count(year)
    
    # sort by year
    year_counts = sorted(year_counts.items(), key = lambda x: x[0])

    counts = [x[1] for x in year_counts]
    years = [x[0] for x in year_counts]

    # create graph and save to a png file
    plt.bar(years, counts)
    plt.title('Total Articles Released Vs Publication Year')
    plt.xlabel('Publication Year')
    plt.ylabel('Total Articles Released')
    plt.savefig('task3b.png')

def task3():
    YEARL = 4 
    MONTHL = 2 
    DAYL = 2
    rows = []
    years = []

    # iterate over the story reviews in the folder
    directory = "/course/data/a1/content/HealthStory/"
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as json_file:
            article = json.load(json_file)

            # only proceed if the publish_date is valid
            publish_date = article["publish_date"]
            if publish_date is None:
                continue
            
            # remove ".json" from the end of the text strings
            news_id = re.sub("(.json)", '', filename)

            # set the variables to constant length of 4, 2, 2 respective
            pub_date = datetime.datetime.fromtimestamp(publish_date)
            year = str(pub_date.year).zfill(YEARL)
            month = str(pub_date.month).zfill(MONTHL)
            day = str(pub_date.day).zfill(DAYL)
            rows.append([news_id, year, month, day])

            # append to a list used for creating the calendar
            years.append(year)
            

    # write and save the the data to a csv file
    with open('task3a.csv', 'w', newline='') as my_csv:
        header = ["news_id", "year", "month", "day"]
        rows = sorted(rows, key = lambda x: x[0])

        writer = csv.writer(my_csv)
        writer.writerow(header)
        writer.writerows(rows)

    # create and save the bar graph
    create_calendar(years)

    return
