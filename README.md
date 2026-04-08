# US-Latam Minerals Policy Research

Comprehensive research and data analysis on US policy toward Latin American minerals, including trade patterns, political agreements, and sustainability practices.

## Project Overview

This project focuses on:
- Analyzing US-Latin America minerals trade patterns
- Tracking policy changes and agreements
- Visualizing mineral resource distributions
- Documenting environmental and sustainability impacts

## Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation
```bash
git clone https://github.com/ChillyLee-lbh/us-latam-minerals-policy.git
cd us-latam-minerals-policy
pip install -r requirements.txt
```

### Usage
```bash
# Run Jupyter notebooks
jupyter notebook notebooks/

# Run analysis scripts
python src/analyzer.py
```

## Project Structure

```
us-latam-minerals-policy/
├── README.md                 # Project overview
├── requirements.txt          # Python dependencies
├── .gitignore
├── data/
│   ├── raw/                 # Raw data files
│   ├── processed/           # Processed datasets
│   └── metadata.json        # Data documentation
├── src/
│   ├── __init__.py
│   ├── data_loader.py       # Data loading utilities
│   ├── analyzer.py          # Analysis functions
│   └── visualization.py     # Visualization tools
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_policy_analysis.ipynb
│   └── 03_trade_patterns.ipynb
├── docs/
│   ├── methodology.md       # Research methodology
│   ├── data_sources.md      # Data sources documentation
│   └── policy_timeline.md   # Policy timeline
└── tests/
    ├── __init__.py
    └── test_analyzer.py     # Unit tests
```

## Data Sources

- USGS Mineral Commodity Summaries
- US Trade Representative (USTR) Reports
- World Bank Open Data
- Academic journals and policy papers
- ECLAC (Economic Commission for Latin America and the Caribbean)

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## License

MIT License - see LICENSE file for details

## Contact

For questions or collaboration, please open an issue or contact the repository maintainer.
