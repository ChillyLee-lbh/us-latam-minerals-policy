"""Analysis module for minerals policy research."""

import pandas as pd
import numpy as np


class MineralsAnalyzer:
    """Analyze minerals trade and policy data."""
    
    def __init__(self, df: pd.DataFrame):
        """Initialize analyzer with a DataFrame."""
        self.df = df.copy()
    
    def summary_statistics(self):
        """Calculate summary statistics."""
        return self.df.describe()
    
    def trade_volume_by_country(self, country_col, value_col):
        """Calculate trade volume by country."""
        return self.df.groupby(country_col)[value_col].sum().sort_values(ascending=False)
    
    def mineral_distribution(self, mineral_col):
        """Get mineral distribution."""
        return self.df[mineral_col].value_counts()
    
    def filter_by_mineral(self, mineral_col, mineral_name):
        """Filter data for specific mineral."""
        return self.df[self.df[mineral_col] == mineral_name]
    
    def get_top_countries(self, country_col, value_col, n=10):
        """Get top n countries by value."""
        return self.df.groupby(country_col)[value_col].sum().nlargest(n)