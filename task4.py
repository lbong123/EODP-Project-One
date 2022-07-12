import json
import csv
import matplotlib.pyplot as plt

def graph_news_data(x_data, y_data):
    """
        takes an x, y input as lists and graphs them on a barh graph
    """

    plt.subplots_adjust(left = 0.32)

    plt.rc('xtick', labelsize= 8) 
    plt.rc('ytick', labelsize= 8) 

    # create graph and save to a png file
    plt.barh(x_data, y_data)
    plt.title('Average Rating Across Varying News Sources')
    plt.xlabel('Average Rating')
    plt.ylabel('News Sources')
    plt.savefig('task4b.png')

def task4():

    news_sources = dict()

    with open('/course/data/a1/reviews/HealthStory.json') as json_file:
        reviews = json.load(json_file)

        for review in reviews:
            
            source = review["news_source"]

            if not source:
                continue

            # create `new_sources` with a tuple (num_articles, avg_rating) value
            if source not in news_sources.keys():
                news_sources[source] = [1, review["rating"]]
            else:
                old_count = news_sources[source][0]
                curr_avg_r = news_sources[source][1]

                news_sources[source][0] += 1
                news_sources[source][1] = (old_count * curr_avg_r + review["rating"]) / (old_count + 1)

        # sort according to news source title
        news_sources = sorted(news_sources.items(), key = lambda x: x[0])

        # combine each key and key-value into a single list
        for i in range(len(news_sources)):
            news_sources[i] = [news_sources[i][0], news_sources[i][1][0], news_sources[i][1][1]]

    # write and save the the data to a csv file
    with open('task4a.csv', 'w', newline='') as my_csv:
        header = ["news_source", "num_articles", "avg_rating"]

        writer = csv.writer(my_csv)
        writer.writerow(header)
        writer.writerows(news_sources)

    # sort according to average rating
    news_sources = sorted(news_sources, key = lambda x: x[2])
    # cut all sources with less than 5 articles
    average_ratings = [x[2] for x in news_sources if x[1] >= 5]
    sources = [x[0] for x in news_sources if x[1] >= 5]
    graph_news_data(sources, average_ratings)

    return





