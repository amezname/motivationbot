import snscrape.modules.twitter as sntwitter
import csv

keyword = 'from:MotivationalUi'
maxTweets = 30000

#Open/create a file to append data to
csvFile = open('tweets.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet']) 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword).get_items()) :
        if i > maxTweets :
            break      
        csvWriter.writerow([tweet.id, tweet.date, tweet.renderedContent])
csvFile.close()