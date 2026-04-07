import pandas as pd
import matplotlib.pyplot as plt
# 1. & 2. Read Dataset and Clean Missing Values
df = pd.read_csv('results.csv')
df = df.dropna()
# 3. Exploring the Dataset
print(f"Total tuples: {len(df)}")
print(f"Unique tournaments: {df['tournament'].nunique()}")
# 4. Convert to Timestamps and Filter for 2018
df['date'] = pd.to_datetime(df['date'])
matches_2018 = len(df[df['date'].dt.year == 2018])
print(f"Matches in 2018: {matches_2018}")
# 5. Team Statistics (Home Team Perspective)
def get_status(row):
    if row['home_score'] > row['away_score']: return 'Win'
    elif row['home_score'] < row['away_score']: return 'Loss'
    else: return 'Draw'
df['status'] = df.apply(get_status, axis=1)
status_counts = df['status'].value_counts()
print(f"Home Team Stats:\n{status_counts}")
# 6. Visualization: Outcome and Neutral Pie Charts
status_counts.plot(kind='pie', autopct='%1.1f%%', title='Home Team Results')
plt.show()
df['neutral'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Neutral Venue Matches')
plt.show()
# 7. Unique Teams
unique_teams = pd.concat([df['home_team'], df['away_team']]).nunique()
print(f"Total unique teams: {unique_teams}")