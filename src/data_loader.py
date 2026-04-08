import pandas as pd

class DataLoader:
    def __init__(self):
        pass

    def load_csv(self, file_path):
        """Loads a CSV file and returns a DataFrame."""
        return pd.read_csv(file_path)

    def load_json(self, file_path):
        """Loads a JSON file and returns a DataFrame."""
        return pd.read_json(file_path)

    def load_excel(self, file_path, sheet_name=0):
        """Loads an Excel file and returns a DataFrame. 
        Specify the sheet name or sheet index to load specific sheets."""
        return pd.read_excel(file_path, sheet_name=sheet_name)