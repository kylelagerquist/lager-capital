import yfinance as yf
import numpy as np


class Markowitz():
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.returns = self.get_returns()
        self.expected_returns = [series.mean() for series in self.returns]
        self.covariance_matrix = np.cov(self.returns)

        print(self.covariance_matrix)


    def get_returns(self):
        all_returns = []
        for ticker in self.tickers:
            stock = yf.Ticker(ticker)
            returns = stock.history(period='max')['Close']
            returns = returns.loc[self.start_date:]
            all_returns.append(returns)
        return all_returns


    # def calc_expected_returns(self):



if __name__ == '__main__':
    Markowitz(['SPY', 'TSLA'], '2020-04-01', '2020-04-01')



