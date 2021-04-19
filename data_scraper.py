from constants import *


class DataScraper:
    def get_most_played_data(self, game_row):
        """Extracts game data from SteamDB Most Played Games table row.
        :type game_row: bs4.element.Tag
        :rtype: dict"""
        # Get Game title
        title = game_row.select("a.css-truncate")[0].get_text()

        # Get Game link
        link = STEAMDB_URL + game_row.select("a.css-truncate")[0]["href"]

        # Get players now
        players_now = game_row.select("td.text-center.green")[0].get_text()

        # Get players peak today
        players_peak_today = game_row.find_all("td", class_="text-center")[1].get_text()

        game_dict = {
            "title": title,
            "link": link,
            "players_now": players_now,
            "players_peak_today": players_peak_today
        }

        return game_dict

    def get_trending_data(self, game_row):
        """Extracts game data from SteamDB Trending games table row.
        :type game_row: bs4.element.Tag
        :rtype: dict"""
        # Get Game title
        title = game_row.select("a.css-truncate")[0].get_text()

        # Get Game link
        link = STEAMDB_URL + game_row.select("a.css-truncate")[0]["href"]

        # Get players now
        players_now = game_row.select("td.text-center.green")[0].get_text()

        game_dict = {
            "title": title,
            "link": link,
            "players_now": players_now,
        }

        return game_dict

    def get_popular_data(self, game_row):
        """Extracts game data from SteamDB Popular Releases table row.
        :type game_row: bs4.element.Tag
        :rtype: dict"""
        # Get Game title
        title = game_row.select("a.css-truncate")[0].get_text()

        # Get Game link
        link = STEAMDB_URL + game_row.select("a.css-truncate")[0]["href"]

        # Get players peak today
        players_peak_today = game_row.select("td.text-center.green")[0].get_text()

        # Price
        price = game_row.find_all("td", class_="text-center")[1].get_text()

        game_dict = {
            "title": title,
            "link": link,
            "players_peak_today": players_peak_today,
            "price": price
        }

        return game_dict

    def get_hot_data(self, game_row):
        """Extracts game data from SteamDB Hot Releases table row.
        :type game_row: bs4.element.Tag
        :rtype: dict"""
        # Get Game title
        title = game_row.select("a.css-truncate")[0].get_text()

        # Get Game link
        link = STEAMDB_URL + game_row.select("a.css-truncate")[0]["href"]

        # Get players peak today
        rating = game_row.select("td.text-center.green")[0].get_text()

        # Price
        price = game_row.find_all("td", class_="text-center")[1].get_text()

        game_dict = {
            "title": title,
            "link": link,
            "rating": rating,
            "price": price
        }

        return game_dict
