import json
import csv
import os

def find_news_title(file_path):
    """
    takes a file_path to an article and returns the title of the news article

    """

    with open(file_path, 'r') as json_file:
        article = json.load(json_file)
        return article['title']



def task2():
    with open('task2.csv', 'w', newline='') as my_csv:
        writer = csv.writer(my_csv)

        # establish header row
        header = ['news_id', 'news_title', 'review_title', 'rating', 'num_satisfactory']
        writer.writerow(header)

        with open('/course/data/a1/reviews/HealthStory.json') as json_file:
            reviews = json.load(json_file)
            
            # loop over the reviews list, to write information about each review
            for review in reviews:
                news_id = review['news_id']

                # finds if the file is stored in the /course/data/a1/content/HealthStory/ sub-folder
                
                file_path = '/course/data/a1/content/HealthStory/' + news_id + '.json'
                
                if not os.path.exists(file_path):
                    continue
                
                # find the title of the original news article
                news_title = find_news_title(file_path)

                review_title = review['title']
                rating = review['rating']
                criteria = review['criteria']
                num_satisfactory = [1 for x in criteria if x['answer'] == 'Satisfactory']

                # write new row
                new_row = [news_id, news_title, review_title, rating, len(num_satisfactory)]
                writer.writerow(new_row)
                
        
    return
