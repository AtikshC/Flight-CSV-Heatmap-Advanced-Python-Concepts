import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#import custom Classes and helper functions

from monthflightdata import MonthFlightData

from yearflightdata import YearFlightData

from HelperFunctions import parse_csv
from HelperFunctions import parse_csv_and_return_monthflightdata
from HelperFunctions import write

from userinputhandler import UserInputHandler
from userinputhandler import NumberInputHandler
from userinputhandler import FeedbackInputHandler
import random
import time

def promp_user_for_year(start_year, end_year):
  """

    Refactoring to make it easier to work with
    _________

    Parameters
    ..........
    start_year: int
      The starting year

    end_year: int
      The ending year

  """

#linear search: worst case scenario is if the element is in the end of the array
#Time complexity: O(n)
def linear_search(data: list[MonthFlightData], year):
  maxPass = -1
  maxMonth = None

  for index in range(0, len(data)):
    month = data[index]
    if month.get_year() == year and month.get_passengers() > maxPass:
      maxPass = month.get_passengers()
      maxMonth = month.get_monthIndex()

  return maxMonth

def linear_search_recursion(data: list[MonthFlightData],
                            index=0,
                            maxPass=-1,
                            maxMonth=None):
   # Invoke the method recursively if there is still the dataset remaining
  if index < len(data):
    month = data[index]
    if month.get_year() == year and month["passengers"] > maxPass:
      maxPass = month.get_passengers()
      maxMonth = month.get_month()
    return linear_search_recursion(year, data, index + 1, maxPass, maxMonth)
  else:
    return maxMonth

#worst scenario: last possible comparison, when algorithm has searched everything by dividing in half with the remainder of the last remaining element which is the target
#Time complexity(log n)
#list of objects, instance of MonthFlightData
def binary_search(data: list[MonthFlightData],year):
  #initialize indiced for lowest and highest point
  low = 0
  high = len(data) - 1
  maxPass = -1
  maxMonth = None

  print(f'low: {low}, high: {high}')
  
  sorted_data = quicksort(data)
  
  while low <= high:
    #calculate middle index
    mid = (low + high) // 2
    print(f'low: {low}, high: {high}, mid: {mid}')
    
    #checking if middle index matches target year 
    if sorted_data[mid].get_year() == year:
      print(f'found year: {sorted_data[mid].get_year()}')
      
      #if passengers greater than maxPass, update maxPass and maxMonth      
      if sorted_data[mid].get_passengers() > maxPass:
        maxMonth = sorted_data[mid].get_monthIndex()
        maxPass = sorted_data[mid].get_passengers()
        print(f'In First If maxMonth: {maxMonth}, maxPass: {maxPass}')
      
      #move to right, search in the higher half now
      low = mid + 1
      print(f'In First If low: {low}, high: {high}, mid: {mid}')
      
      #if middle element less than tagret year, search in right half
    elif sorted_data[mid].get_year() < year:
      low = mid + 1
      print(f'Under elif low: {low}, high: {high}, mid: {mid}')
      
      #if middle element more than target year, search in left half
    else:
      high = mid - 1
      print(f'In else high: {high}, low: {low}, mid: {mid}')
      
  return maxMonth

year_input_handler = NumberInputHandler("Select a year from 1949-1960 : ",
                                        lambda x: 1949 >= int(x) >= 1960)

sortInput = NumberInputHandler("Select 1 for quick, 2 for bubble, 3 for selection : ", lambda x: 1 >= int(x) >= 3)

targetYear = int(year_input_handler.prompt_for_input(1949,1960))

sortingPrompt = int(sortInput.prompt_for_input(1,3))

year_input_handler.process_input()

#import csv
flightGraph = parse_csv("flights.csv")

month_flight_data = parse_csv_and_return_monthflightdata("./flights.csv")

sorted_passengers = flightGraph['passengers'].tolist()

#shuffled_dataset = flightGraph.sample(frac=1).reset_index(drop=True)

#Quick Sort:

#Time Complexity: Worst case -O(n^2), average case - n log n, best n log n
#recursive, less and less loops to check, iterations increase
#The worst-case scenario occurs when the chosen pivot always results in highly unbalanced partitions, leading to essentially no reduction in the problem size.
def quicksort(data: list[MonthFlightData]):
  #dont need to sort if less than one
  if len(data) <= 1:
    return data
    
  pivot = data[len(data) // 2].get_passengers()
  #for loop in list to create list of smaller and larger elements
  left = [x for x in data if x.get_passengers() < pivot] #creates list of items less than pivot, returns x if x < pivot
  middle = [x for x in data if x.get_passengers() == pivot]#create list  of item equal to pivot
  right = [x for x in data if x.get_passengers() > pivot]#creates list of items greater to pivot
  #only for right and left list, middle quicksort order doesnt matter
  #recursively breaking down problem into smaller chunks
  #call until broken down into 1
  return quicksort(left) + middle + quicksort(right)

#Worst Case Time Complexity: O(n^2)
#The worst-case scenario occurs when the input array is in reverse order, and each element needs to be swapped in every pass.
def bubbleSort(data:list[MonthFlightData]):
  for i in range(len(data)):
    for j in range(0, len(data) - i - 1):
      if data[j].get_passengers() > data[j + 1].get_passengers():
        data[j], data[j + 1] = data[j + 1], data[j]
  return data

#Selection Sort:

#Worst Case Time Complexity: O(n^2)
#The worst-case scenario is similar to Bubble Sort, where the input array is in reverse order, and the algorithm needs to repeatedly find and swap the minimum element.
def selectionSort(data:list[MonthFlightData]):

  for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j].get_passengers() < data[min_index].get_passengers():
        min_index = j
    data[i], data[min_index] = data[min_index], data[i]
  return data

#write(str(shuffled_dataset['passengers'].tolist()), "unsorted1.txt", "w")

if sortingPrompt == 1:
  startTime = time.time()
  sorted_passengers = quicksort(month_flight_data)
  endTime = time.time()

  elapsed = endTime - startTime

  print(f"Time for quick sort was {elapsed}")

  write(str(sorted_passengers), "quickSort.txt", "w")
  
if sortingPrompt == 2:
  bubbleTime = time.time()
  bubbleSorted = bubbleSort(month_flight_data)
  bubbleEnd = time.time()
  
  bubbleElapse = bubbleEnd - bubbleTime
  
  write(str(bubbleSorted), "bubbleSort.txt", "w")
  
  print(f"Time for bubble sort was {bubbleElapse}")

if sortingPrompt == 3:
  selectionTime = time.time()
  sortedSelection = selectionSort(month_flight_data)
  selectionEnd = time.time()
  
  selectionElapse = selectionEnd - selectionTime
  
  print(f"Time for selection sort was {selectionElapse}")
  
  write(str(sortedSelection), "selectionSort.txt", "w")
  
dataset = flightGraph["passengers"].tolist()
totalPassengers = flightGraph["passengers"].sum()

year_flight_data = {}

#iterate through csv rows for year month and passengers to get values
for index, row in flightGraph.iterrows():
  Year = row['year']
  month = row['month']
  passengers = row['passengers']

  if Year not in year_flight_data:
    year_flight_data[Year] = YearFlightData(Year)

  monthIndex = pd.to_datetime(month, format='%B', errors='coerce').month

  monthData = MonthFlightData(passengers, month, Year)
  year_flight_data[Year].addMonth(monthData)

averagePass = year_flight_data[targetYear].yearlyAvg()
dailyPass = year_flight_data[targetYear].dailyAvg()

#calculate both average passengers and outliers

##moduloPass = sumPassenger % 12

##averagePass = (sumPassenger/12)

#avgPass = f"Average Passengers for {int(targetYear)}: {int(averagePass): .2f}"

print(f"Average number of passengers per year {averagePass}")
print(f"Average number of passengers per day {dailyPass}")

maxPrompt = NumberInputHandler("Would you want to know the month which had the max passengers during this year, press 1 for yes, 2 for no?", lambda x: 1 >= int(x) >= 2)

maxUser = int(maxPrompt.prompt_for_input(1,2))

if maxUser == 1:
  
  linearTime = time.time()
  max_month = linear_search(month_flight_data, targetYear)
  #max_month = linear_search_recursion(targetYear, flightGraph, 0, -1, None)
  linearEnd = time.time()
  
  linearElapsed = linearEnd - linearTime
  
  recurTime = time.time()
  max_month_recur = linear_search_recursion(month_flight_data, targetYear)
  recurEnd = time.time()
  
  recurElapse = recurEnd - recurTime
  
  print(f"Using recursion, max passengers during {targetYear} was {max_month_recur}")
  
  print(f"Time for recursive was {recurElapse}")
  
  print(
      f"The month with the max passengers during {targetYear} using linear search was {max_month}"
  )
  print(f"The time for linear was {linearElapsed}")
  
  binaryTime = time.time()
  binaryMonth = binary_search(month_flight_data, targetYear)
  binaryEnd = time.time()
  binaryElapsed = binaryEnd - binaryTime
  
  print(
      f"The month with the max passengers during {targetYear} using binary search was {max_month}"
  )
  print(f"The time for binary was {binaryElapsed}")

#outlier = "The number of outliers for the year was " + str(moduloPass)

#print(outlier)

#write the results

write(str(averagePass), "./Results.txt")

#write(outlier,"./Results.txt","a")

percent = (averagePass / totalPassengers) * 100

percent = round(percent, 2)

print(f"Total passengers in the whole dataset {totalPassengers}")

percentOfpassengers = "The percent of the passengers for the chosen year versus total passengers was " + str(
    percent) + "%"

print(percentOfpassengers)

write(percentOfpassengers, "./Results.txt", "a")

print("The results for this test have been recorded")
#Question the user for feedback to write to results
"""
while True:
  UserYear = input("Please enter a year that we don't currently have to be used in our dataset")

  try: 
    UserYear = int(UserYear)
    if 1900 <= UserYear <= 2023:
      break
    else:
      print("Not a valid year")
  except ValueError:
    print("Invalid input.")


while True:
  userMonth = input("Please enter a month for the year from 1-12")
  try:
    userMonth = int(userMonth) 
    if 1 <= userMonth <= 12:
      break
    else:
      print("Invalid month number")
  except ValueError:
    print("Invalid input.")

userPassenger = input("Please enter the numbers of passengers for that year and month that we don't currently have to be used in our dataset")

while True:
  try:
   userPassenger = int(userPassenger)
   break  # Break the loop if the input is an integer
  except ValueError:
   print("Invalid input. Please enter a valid integer for the number of passengers.")
   userPassenger = input("Please enter the numbers of passengers for that year and month that we don't currently have to be used in our dataset")
"""

feedback_handler = FeedbackInputHandler(
    f"Please enter a year, month, and passenger amount we dont have to add to our csv: "
)

user_feedback = feedback_handler.prompt_for_input()

feedback_handler.provide_feedback()

feedback_parts = user_feedback.split()

if len(feedback_parts) == 3:
  try:
    userYear, userMonth, userPassenger = map(int, feedback_parts)
  except:
    print("Invalid input")
    userYear, userMonth, userPassenger = 0, 0, 0
else:
  print("Invalid format")
  userYear, userMonth, userPassenger = 0, 0, 0

print("Thank you for your feedback! It has been recorded in the dataset")

feedbackMsg = f"{userYear}, {userMonth}, {userPassenger}"

#write feedback to results

write(feedbackMsg, "./Results.txt", "a")

#reading final results back to user for file
results = parse_csv("Results.txt")

print("Your final results were: " + results)

#Calculating Monthly averages

#Graph starts here

flightMatrix = flightGraph.pivot_table(index="year",
                                       columns="month",
                                       values='passengers')

months = flightMatrix.columns.astype(str)
years = flightMatrix.index.astype(str)

plt.figure(figsize=(10, 6))
heatMap = plt.imshow(flightMatrix,
                     cmap='coolwarm',
                     aspect="auto",
                     origin="lower")

for i in range(len(flightMatrix)):
  for j in range(len(flightMatrix.columns)):
    plt.text(j,
             i,
             f'{flightMatrix.values[i,j]: .1f}',
             ha="center",
             va="center",
             color='w',
             fontsize=10)

plt.yticks(range(len(months)), months)
plt.xticks(range(len(years)), years)

plt.colorbar(heatMap)
plt.title("Heatmap of flights")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()
