import pandas as pd

# Load raw data
climate_data = pd.read_csv('data/raw/Crop_recommendation.csv')

# Drop missing values
climate_data = climate_data.dropna()

# Normalize temperature
climate_data['temperature'] = (climate_data['temperature'] - climate_data['temperature'].min()) / \
                              (climate_data['temperature'].max() - climate_data['temperature'].min())

# Save processed data
climate_data.to_csv('data/processed/climate_cleaned.csv', index=False)
