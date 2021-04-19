import pandas as pd
import json


class DataWriter:
    def write_to_csv(self, data, filename):
        """Writes list of dictionaries to CSV.
        :type data: list[dict]
        :type filename: str"""
        df = pd.DataFrame(data)
        df.to_csv(filename + ".csv")

    def write_to_json(self, data, filename):
        """Writes list of dictionaries to JSON.
        :type data: list[dict]
        :type filename: str"""
        with open(filename + ".json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
