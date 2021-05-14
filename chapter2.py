import pandas as pd
import matplotlib.pyplot as plt

scientist = pd.read_csv("data/scientists.csv")

born_date_time = pd.to_datetime(scientist['Born'], format = '%Y-%m-%d')
print(born_date_time)
print(type(born_date_time))