from pytrends.request import TrendReq
from datetime import datetime

pytrends = TrendReq(hl='en-US', tz=300)

today = datetime.today()
current_year = today.strftime('%Y')
current_month = today.strftime('%m')
current_day = today.strftime('%d')
current_hour = today.strftime('%H')

# get the average for a word over a dataset returned from pytrends
def get_average(data, word):
	data_size = round(data.size / 3)

	average = 0
	for i in range(data_size):
		num = data.iat[i, 1]
		average = average + num

	average = average / data_size
	return average

# assemble the api request and get the average for a word
# defaults to current year, month, day, hour
def get_google_search_avg(
		word,
		year=current_year,
		month=current_month,
		day=current_day,
		hour='00',
		year2=current_year,
		month2=current_month,
		day2=current_day,
		hour2=current_hour,
		alternative_timeframe=None):
	timeframe = None
	if alternative_timeframe != None:
		timeframe = alternative_timeframe
	else:
		timeframe = f'{year}-{month}-{day}T{hour} {year2}-{month2}-{day2}T{hour2}'

	pytrends.build_payload([WORD], cat=0, timeframe=timeframe, geo='', gprop='')

	data = pytrends.interest_over_time()
	data = data.reset_index()

	return get_average(data, word)

# get the historical average for a word
# (looks at data from 2019 to 2021 for a day from each month from 0 hours up to the specified hour)
def get_historical_avg(word, year=current_year, hour=current_hour):
	average = 0

	year_count = 3
	min_year = int(year) - year_count
	max_year = int(year)

	for year in range(min_year, max_year):
		for month in range(1, 12):
			month_formatted = str(month).zfill(2)
			day_avg = get_google_search_avg(word, year=year, month=month_formatted, day='01', year2=year, month2=month_formatted, day2='01', hour2=hour)
			print(day_avg)
			average = average + day_avg

	return average / (year_count * 12)

# change these here
WORD = 'being'
YEAR = '2022'
MONTH = '05'
DAY = '10'
HOUR = '12'

historical_avg = get_historical_avg(WORD, hour=HOUR)
wordle_day_avg = get_google_search_avg(WORD, day=DAY, day2=DAY, hour2=HOUR)

print("historical avg: ", historical_avg)
print("day of avg: ", wordle_day_avg)
