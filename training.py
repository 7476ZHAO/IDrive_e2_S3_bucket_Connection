from data_loader import load_data
from model import train

df = load_data()   # retrieve data
train(df)          # training model