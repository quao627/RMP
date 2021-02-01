import pandas as pd

school = pd.read_csv("School/Vanderbilt.csv")
prof_id = 2197326
print(school.loc[school.tid == 2197326, "tNumRatings"])