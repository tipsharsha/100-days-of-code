"""Goes back to the old days"""
from bs4 import BeautifulSoup

x = input("What day do you want to go back to?(Format DD-MM-YYYY)   ")
Date = int(x[0:2])
Month = int(x[3:5])
Year = int(x[6:10])
print(Date,Month,Year)
