import tweepy
import json
import requests


class MyStreamListener(tweepy.StreamListener):

    stock_list = []
    stock_id_pair = {}
    stock_list_of_tweets_pair = {}
    stock_sentiment_score_pair = {}
    totalTweetsParsed = 1

    def on_status(self, status):

        for stock in self.stock_list:
            self.stock_id_pair.update({stock, 1})
            self.stock_list_of_tweets_pair.update({stock, ""})
            self.stock_sentiment_score_pair.update({stock, 0})

        if self.totalTweetsParsed % 900 == 0:
            self.process_sentiment_on_list()
            self.publish_to_powerbi_and_twitter()
            for stock in self.stock_list:
                self.stock_list_of_tweets_pair.update({stock, ""})

        for stock in stock_list:
            if stock in str(status.text):
                texts = {'language': 'en'}
                texts['id'] = self.stock_id_pair[stock]
                self.stock_id_pair[stock]+=1

                texts['text'] = status.text
                self.stock_list_of_tweets_pair[stock].append(texts)
        self.totalTweetsParsed += 1

    def process_sentiment_on_list(self):
        for stock in self.stock_list:
            list_of_tweets = self.stock_list_of_tweets_pair[stock]
            if list_of_tweets:
                document = {'documents': list_of_tweets}
                scores = self.get_scores(document)
                total_score = 0

                if scores is not None:
                    for i in range(len(scores)):
                        score = scores[i]['score']
                        total_score+= score

                overall_sentiment_score =  total_score/ len(self.get_scores(document))
                self.stock_sentiment_score_pair[stock] = overall_sentiment_score

    def get_scores(self, document):
        response = requests.post(self.sentiment_api_url, headers=self.sentiment_api_headers, json=document)
        result = response.json()
        scores = json.loads(json.dumps(result))
        if 'documents' in scores:
            return scores['documents']

        return None

    def rebalance_stocks(self):
        for stock in self.stock_list:
            if self.stock_sentiment_score_pair[stock] > 0.66:
                # buy
            else:
                # sell
        print('success!')
