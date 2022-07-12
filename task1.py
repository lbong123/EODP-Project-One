import json
import os

def task1():
    # find the number of articles
    dir_path = '/course/data/a1/content/HealthStory/'
    no_articles = len(os.listdir(dir_path))

    # find the number of reviews
    with open('/course/data/a1/reviews/HealthStory.json') as json_file:
        reviews = json.load(json_file)
        no_reviews = len(reviews)

    # find the total number of tweets, then remove duplicates
    with open('/course/data/a1/engagements/HealthStory.json') as json_file:
        reviews = json.load(json_file)
        total_tweets = []

        for story in reviews.keys():
            total_tweets += reviews[story]["tweets"]
            total_tweets += reviews[story]["retweets"]
            total_tweets += reviews[story]["replies"]
                
        no_tweets = len(set(total_tweets))
    
    # create and convert dict into json file
    task_one_dict = {
        "Total number of articles": no_articles,
        "Total number of reviews": no_reviews,
        "Total number of tweets": no_tweets,
    }
    
    with open('task1.json', 'w') as json_file:
        json.dump(task_one_dict, json_file)

    return None





