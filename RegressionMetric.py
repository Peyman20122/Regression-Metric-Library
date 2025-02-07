class MetricRegLearn:
    def __init__(self,r2,mape):
        self.r2score = r2
        self.mape = mape
    def metric(self):
        final_score = ((1 - self.mape) + self.r2score) / 2 * 100
        return final_score

