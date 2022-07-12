import json
import os
import re
from nltk.corpus import stopwords

def task6():

    directory = "/course/data/a1/content/HealthStory/"
    all_words = dict()

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as json_file:
            article = json.load(json_file)
            # perform steps 1 - 5
            text = article["text"]
            text = re.sub(r'[^a-zA-Z\s\t\n]', ' ', text)
            text = re.sub(r'[\t\n]', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            text = text.lower()
            tokens = re.split(" ", text)
             
            # remove stop words and words of length < 1
            stop_words = set(stopwords.words('english'))
            tokens = filter(lambda x: x not in stop_words, tokens)
            tokens = list(filter(lambda x: len(x) > 1, tokens))
            
            news_id = re.sub("(.json)", "", filename)
            
            for token in tokens:
                if token not in all_words.keys():
                    all_words[token] = [news_id]
                elif news_id not in all_words[token]:
                    all_words[token].append(news_id)
    
    # sort the articles list for each token 
    for token in all_words.keys():
        all_words[token] = sorted(all_words[token])

    # sort the dictionary by tokens
    all_words = dict(sorted(all_words.items(), key = lambda x: x[0]))
    
    # export to a json file
    with open('task6.json', 'w') as json_file:
        json.dump(all_words, json_file)


    return
