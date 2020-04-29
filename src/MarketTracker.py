class MarketTracker:

    def __init__(self):
        self.tracker = {}
        self.trackerSnapshot = []
        self.trackerIndex = 0
    
    def Update(self, price_changes, lookBackLimit = 3,  tickBounds = [0.33, 0.67]):
        stocksToBuy = {}
        stocksToKeep = {}
        stocksToSell = {}

        positive_changes = {k: v for k, v in price_changes.items() if v >0}
        negative_changes = {k: v for k, v in price_changes.items() if v <=0}

        for symbol in positive_changes:
            if not self.tracker[symbol]:
                self.tracker[symbol] = {"positive": 0, "negative": 0}
                self.trackerSnapshot[symbol] = []
            self.tracker[symbol].positive += 1
            self.tracker[symbol].negative -= 1
            self.trackerSnapshot[symbol].append(self.tracker[symbol]) #Save to snapshot        

        for symbol in negative_changes:
            if not self.tracker[symbol]:
                self.tracker[symbol] = {"positive": 0, "negative": 0}
                self.trackerSnapshot[symbol] = []
            self.tracker[symbol].positive -= 1
            self.tracker[symbol].negative += 1
            self.trackerSnapshot[symbol].append(self.tracker[symbol]) #Save to snapshot        
        
        if self.trackerIndex < lookBackLimit: return stocksToSell, stocksToBuy, stocksToKeep
        #calculate
        for symbol in price_changes:
            history = self.trackerSnapshot[symbol][-lookBackLimit:]
            latest_history = history[-1]

            #traverse from latest and check for number of upticks or downticks of the stock
            upticks = 0
            downticks = 0
            for item in history[::-2]:
                upticks +=  1 if (latest_history.positive - item.positive) == 1 else 0
                downticks += 1 if (latest_history.negative - item.negative) == 1 else 0
                latest_history = item

            uptickPercentage = float(upticks/lookBackLimit)
            if uptickPercentage < tickBounds[0] :
                stocksToSell[symbol] = price_changes[symbol]
            elif uptickPercentage> tickBounds[0] and uptickPercentage < tickBounds[1]:
                stocksToBuy[symbol] = price_changes[symbol]
            else:
                stocksToKeep[symbol] = price_changes[symbol]
                
        return stocksToSell, stocksToBuy, stocksToKeep


    def RestTracker(self):
        self.tracker = {}
        self.trackerSnapshot = []
        self.trackerIndex = 0





        

    