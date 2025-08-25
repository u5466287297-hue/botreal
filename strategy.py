
import random, datetime

class Bot:
    def __init__(self):
        self.signal = "NO_SIGNAL"
        self.confidence = 0
        self.stats = {
            "today_signals":0,
            "today_buy":0,
            "today_sell":0,
            "today_accuracy":0.0,
            "win":0,
            "loss":0,
            "accuracy":0.0
        }
        # store chart data (candles + signals)
        self.chart_data = {
            "times":[],
            "opens":[],
            "highs":[],
            "lows":[],
            "closes":[],
            "buys":[],
            "sells":[]
        }

    def update(self):
        # Dummy: generate one new candle & maybe signal
        now = datetime.datetime.utcnow()
        t = now.isoformat()
        o = random.uniform(100,110)
        c = o + random.uniform(-2,2)
        h = max(o,c) + random.random()
        l = min(o,c) - random.random()
        self.chart_data["times"].append(t)
        self.chart_data["opens"].append(o)
        self.chart_data["highs"].append(h)
        self.chart_data["lows"].append(l)
        self.chart_data["closes"].append(c)
        sig = "NO_SIGNAL"
        if random.random()<0.3:
            sig = "BUY"
        elif random.random()<0.6:
            sig = "SELL"
        self.signal = sig
        self.confidence = int(70+random.random()*20)
        if sig=="BUY":
            self.stats["today_signals"]+=1
            self.stats["today_buy"]+=1
            self.chart_data["buys"].append(len(self.chart_data["closes"])-1)
        elif sig=="SELL":
            self.stats["today_signals"]+=1
            self.stats["today_sell"]+=1
            self.chart_data["sells"].append(len(self.chart_data["closes"])-1)
        else:
            self.chart_data["buys"].append(None)
            self.chart_data["sells"].append(None)
        # update accuracy stats (dummy)
        w = random.randint(0,1)
        self.stats["win"] += w
        self.stats["loss"] += 1-w
        tot = max(1,self.stats["win"]+self.stats["loss"])
        self.stats["accuracy"] = round(100*self.stats["win"]/tot,2)
        self.stats["today_accuracy"] = self.stats["accuracy"]
