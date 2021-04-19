from bs4 import BeautifulSoup
import requests
from data_scraper import DataScraper
from data_writer import DataWriter


# Setting up and making soup -------------------------------------------------------------------------------------------

headers = {
    "Accept-Language": "en-GB,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
}
response = requests.get("https://steamdb.info/", headers=headers)
webpage = response.text

# Make soup
soup = BeautifulSoup(webpage, "html.parser")

# Processing soup ------------------------------------------------------------------------------------------------------

# Every div with class span6 encapsulates one category, there are four categories
groups = soup.find_all("div", class_="span6")

# Splitting into separate groups

# Starting from 1, 0 position is an empty row
most_played = groups[0].select("tr.app")[1:]
# Starting from 0 - the first row
trending = groups[1].select("tr.app")
# Starting from 0 - the first row
popular = groups[2].select("tr.app")
# Starting from 0 - the first row
hot_releases = groups[3].select("tr.app")

# Scraping -------------------------------------------------------------------------------------------------------------

data_scraper = DataScraper()
data_writer = DataWriter()

# Processing Most Played
most_played_data = []

for game_row in most_played:
    most_played_data.append(data_scraper.get_most_played_data(game_row))

data_writer.write_to_csv(most_played_data, "most_played")
# data_writer.write_to_json(most_played_data, "most_played")

# Processing Trending
trending_data = []

for game in trending:
    trending_data.append(data_scraper.get_trending_data(game))

data_writer.write_to_csv(trending_data, "trending")
# data_writer.write_to_json(trending_data, "trending")

# Processing Popular
popular_data = []

for game in popular:
    popular_data.append(data_scraper.get_popular_data(game))

data_writer.write_to_csv(popular_data, "popular")
# data_writer.write_to_json(popular_data, "popular")

# Processing Hot Releases
hot_releases_data = []

for game in hot_releases:
    hot_releases_data.append(data_scraper.get_hot_data(game))

data_writer.write_to_csv(hot_releases_data, "hot_releases")
# data_writer.write_to_json(hot_releases_data, "hot_releases")
