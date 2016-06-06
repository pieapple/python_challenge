import calendar
from datetime import date

def solve():
  for i in range(96, 1996, 10):
    if calendar.isleap(i) and date(i, 1, 1).weekday() == 3:
      print i

if __name__ == "__main__":
  solve()
