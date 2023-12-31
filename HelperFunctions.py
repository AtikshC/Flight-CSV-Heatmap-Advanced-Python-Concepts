from monthflightdata import MonthFlightData
import pandas as pd
import csv


def parse_csv(filePath):
  """
  Parses the csv and spits it out
  _______

  Attributes
  .........
  filePath: Csv file
    takes in a file to read

  _________

  Returns: Csv File
    Returns the csv file

  """
  parsedCsv = pd.read_csv(filePath)
  return parsedCsv


def write(newData, newPath, mode='w'):
  """
  Writes data into another csv file
  _______

  Attributes
  .........
  newData: any
    Takes in the data to be written

  newPath: Csv File
    Location to be written

  mode: File mode
    Mode for the data to be written in
  """
  with open(newPath, mode) as file:
    file.write(newData)


def parse_csv_and_return_monthflightdata(file_path) -> list[MonthFlightData]:

  with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    next(reader)  # Skip the header row
    monthflightdata = []
    for row in reader:
      print(row)
      monthflightdata.append(MonthFlightData(row['passengers'], row['month'], row['year']))
    return monthflightdata
