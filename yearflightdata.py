class YearFlightData:
  """
  Used to store data for a year's worth of fligth data

  ---

  Atributes
  .........

  year:int
    The year of the flight data

  months:lists[monthData]
    List of month data
  
  ___

  Methods
  .......

  addMonth(monthData)
    Add monthData to months[]

  
  
  """
  def __init__(self,year):
    """
    Constructs neccesary attributes for YearFlightData object

    ___

    Parameters
    ..........
    year:int
      The year of the flight data

    
    """
    self.__year = year
    self.__months = []
  
  

  def addMonth(self, monthData):
    """
    Add monthData to months

    _______

    Parameters
    ..........
    monthData: MonthData
      Instance of monthData

    
    """
    self.__months.append(monthData)

  
  def get_year(self):
    """
    Gets the year

    ___

    Returns: int
    ............
      Returns the year
    
    """
    return self.__year

  def get_months(self):
    """
    Gets the months

    ___

    Returns: List[]
    ............
      Returns the months
    
    """
    return self.__months


  
  def yearlyAvg(self):
    """
    Calculates the yearly average
    ___

    Returns: int
    ............
      Returns the avg passengers per month
    """
    totalPassengers = 0
    for month in self.__months:
     
      totalPassengers += month.get_passengers()

    totalPassengers = totalPassengers/12
    return int(totalPassengers)
    

  def dailyAvg(self):
    """
    Calculates the daily average
    ___
    """
    total_passengers= 0
    for month in self.__months:
      total_passengers += month.get_passengers()
    return int(total_passengers/365)