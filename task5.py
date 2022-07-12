import json
import matplotlib.pyplot as plt

def group_by_ratings(directory):
    """
        Takes a reviews list and groups the articles by rating
    """
    ratings = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }

    with open(directory) as json_file:
        reviews = json.load(json_file)
        for review in reviews:
            ratings[review["rating"]].append(review["news_id"])
        
    return ratings

def graph_news_data(x_data, y_data):
    """
        takes an x, y input as lists and graphs them on a bar graph
    """
    plt.rc('xtick', labelsize= 10) 
    plt.rc('ytick', labelsize= 10) 

    # create graph and save to a png file
    plt.scatter(x_data, y_data)
    plt.title('Average Number of Tweets vs Article Rating')
    plt.xlabel('Article Rating')
    plt.ylabel('Average Number of Tweets')
    plt.savefig('task5.png')

def task5():
    directory = "/course/data/a1/reviews/HealthStory.json"
    ratings = group_by_ratings(directory)

    with open('/course/data/a1/engagements/HealthStory.json') as json_file:
        reviews = json.load(json_file)
        group_num = [0, 1, 2, 3, 4, 5]
        average_tweets = []

        # iterate over ratings dictionary
        for group in ratings.keys():
            average_per_group = []

            # find the average tweets per rating category
            for article in ratings[group]:
                if article in reviews.keys():
                    curr_tweets = []
                    curr_tweets += reviews[article]["tweets"]
                    curr_tweets += reviews[article]["retweets"]
                    curr_tweets += reviews[article]["replies"]

                    curr_tweets = len(set(curr_tweets))
                    average_per_group.append(curr_tweets)

            average_tweets.append(sum(average_per_group)/len(average_per_group))
            
        graph_news_data(group_num, average_tweets)

    return
