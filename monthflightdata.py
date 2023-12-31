from calendar import monthrange
from datetime import datetime


class MonthFlightData:

  def __init__(self, passengers, monthName, year):
    """

    Constructs neccesary attributes for MonthFlightData object

    ___

    Parameters
    ..........
    passengers:int
      The passenger data in flight data

    monthName: str
      Name of all months in flight data

    monthIndex: int
      Index of all months in flight data


    """
    self.__passengers = int(passengers)
    self.__monthName = monthName
    self.__year = int(year)
    self.__monthIndex = datetime.strptime(monthName.lower(), '%B').month

  def get_year(self):
    """
    Gets the passengers

    ___

    Returns: int
    ............
      Returns the year
    """
    return self.__year

  def get_passengers(self):
    """
    Gets the passengers

    ___

    Returns: int
    ............
      Returns the passengers

    """
    return self.__passengers

  def get_monthName(self):
    """
    Gets the monthName

    ___

    Returns: str
    ............
      Returns the monthName

    """
    return self.__monthName

  def get_monthIndex(self):
    """
    Gets the monthIndex

    ___

    Returns: int
    ............
      Returns the monthIndex

    """
    return self.__monthIndex

  def dailyAvg(self, year):
    """
    Calculates the daily average of passengers
    ___

    Returns: int
    ............
      Returns the average amount of passengers per day
    """
    # returns a tuple of (0-6 ~ Mon-Sun) and number of days (28-31) for the month.

    days_in_month = monthrange(int(year), self.__monthIndex)[1]
    dayAvg = self.__passengers / days_in_month
