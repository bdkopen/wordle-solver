from pytrends.request import TrendReq

def get_average(data, word):
	data_size = round(data.size / 3)

	average = 0
	for i in range(data_size):
		num = data.iat[i, 1]
		average = average + num

	average = average / data_size
	return average

pytrends = TrendReq(hl='en-US', tz=360)

WORD = 'scrap'
kw_list = [WORD]

pytrends.build_payload(kw_list, cat=0, timeframe='2022-05-21T00 2022-05-21T04', geo='', gprop='')
data = pytrends.interest_over_time()
data = data.reset_index()

print("Average today: ", get_average(data, WORD))

pytrends.build_payload(kw_list, cat=0, timeframe='2021-05-21T00 2021-05-21T04', geo='', gprop='')
data = pytrends.interest_over_time()
data = data.reset_index()

print("Average last year: ", get_average(data, WORD))
