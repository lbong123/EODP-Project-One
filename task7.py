import json
import os
import re
import numpy
import csv
import matplotlib.pyplot as plt

def prob(word, word_list, news_list):
    """ 
    finds and returns the probability that a word w in our vocabulary
    appears in a real/fake news article.

    """

    containing_w = word_list[word]
    containing_w = [x for x in containing_w if x in news_list]
 
    return len(containing_w)/len(news_list)

def odd(prob_w):
    """ 
    finds and returns the odds that a word w in our vocabulary
    appears in a real/fake news article given the probability of w.

    """
    return prob_w / (1 - prob_w)


def graph_histogram(log_odds_ratios):
    # lines 31-40 have been referenced from 
    # https://stats.stackexchange.com/questions/798/calculating-optimal-number-of-bins-in-a-histogram
    # define array of data
    data = numpy.array([x[1] for x in log_odds_ratios])

    # calculate interquartile range 
    q3, q1 = numpy.percentile(data, [75 ,25])
    IQR = q3 - q1

    # using the Freedman-Diaconis rule
    h = 2 * IQR * (len(data) ** -(1/3))
    optimal_bins = round((max(data) - min(data)) / h)

    plt.hist(data, bins = optimal_bins)
    plt.title('Frequencies of Log_Odd_Ratios Across All Words')
    plt.xlabel('Log_Odd_Ratios')
    plt.ylabel('Frequency')
    plt.savefig('task7b.png')
    plt.close()

def graph_news_data(x1, x2, y1, y2):
    """
        takes an x, y input as lists and graphs them on a bar graph
    """
    
    # create graph and save to a png file
    fig, axs = plt.subplots(2)

    fig.suptitle('Highest and Lowest Odd Ratios across all Words', fontsize = 20)
    fig.set_size_inches(10, 8)

    # set labels for first graph
    axs[0].barh(x1, y1)
    axs[0].set_xlabel('Odds Ratio', fontsize = 13)
    axs[0].set_ylabel('Word', fontsize = 13)

    # set labels for the second graph
    axs[1].barh(x2, y2)
    axs[1].set_xlabel('Odds Ratio', fontsize = 13)
    axs[1].set_ylabel('Word', fontsize = 13)

    # set tick sizes for axes
    axs[0].tick_params(axis='both', labelsize = 10)
    axs[1].tick_params(axis='both', labelsize = 10)

    plt.savefig('task7c.png')
    
    

def task7():

    with open('/home/task6.json') as json_file:
        word_list = json.load(json_file)

    fake_news = []
    real_news = []
    REAL_THRESHHOLD = 3
  
    with open('/course/data/a1/reviews/HealthStory.json') as json_file:
        reviews = json.load(json_file)

    # categorise articles as either fake or real news
    for review in reviews:
        news_id = review["news_id"]
        file_path = '/course/data/a1/content/HealthStory/' + news_id + '.json'

        if not os.path.exists(file_path):
            continue
        
        if review["rating"] < REAL_THRESHHOLD:
            fake_news.append(news_id)
        else:
            real_news.append(news_id)

    log_odds_ratios = []
    odds_ratios = []
    words = []

    # assign probabilities and odds to each word
    for word in word_list.keys():
        prob_fake = prob(word, word_list, fake_news)
        prob_real = prob(word, word_list, real_news)

        # skip words which have need to be excluded as per the task
        if prob_fake in [0, 1] or prob_real in [0, 1]  \
            or len(word_list[word]) == len(fake_news) + len(real_news) \
            or len(word_list[word]) < 10:

            continue
            
        # calculate logs and odds ratios
        odds_ratio = odd(prob_fake) / odd (prob_real)
        log_odds_ratio = round(numpy.log10(odds_ratio), 5)

        # append ratios to two lists
        odds_ratios.append([word, odds_ratio])
        log_odds_ratios.append([word, log_odds_ratio])

    # write and save the the data to a csv file
    with open('task7a.csv', 'w', newline='') as my_csv:
        header = ["word", "log_odds_ratio"]

        writer = csv.writer(my_csv)
        writer.writerow(header)
        writer.writerows(log_odds_ratios)
    
    # sort task7c data
    odds_ratios = sorted(odds_ratios, key = lambda x: x[1])
    odds_ratios = odds_ratios[:15] + odds_ratios[-15:]
    words = [x[0] for x in odds_ratios]
    odds_ratios = [x[1] for x in odds_ratios]

    graph_histogram(log_odds_ratios)
    graph_news_data(words[:15], words[15:], odds_ratios[:15], odds_ratios[15:])
    

    return


