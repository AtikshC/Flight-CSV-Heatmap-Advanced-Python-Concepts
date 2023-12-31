class UserInputHandler:
  def __init__(self, prompt):
    self.__prompt = prompt
    
  #these will be overriden in the child class
  def prompt_for_input(self):
    raise NotImplementedError("One of the subclasses must implement prompt method")

  def validateInput(self):
    raise NotImplementedError("One of the subclasses must implement validate method")  

  def getting_user_input(self, prompt):
    return input(prompt)

  def get_prompt(self):
    return self.__prompt
    
class NumberInputHandler(UserInputHandler):
  def __init__(self, prompt, validation_function):
    super().__init__(prompt)
    self.__validation_function = validation_function
    self.__input_value = None
    
  def prompt_for_input(self,x,y):
    while True:
      
      userInput = input(self.get_prompt())

      if self.validateInput(userInput,x,y):
        self.__input_value = int(userInput)
        return userInput
      else:
        print("Try again")
      

  def validateInput(self, input,x,y):
    try:
      if(int(input) >= x and int(input) <= y):

        return True
    except: 
      return False
    
  
  def get_validation_function(self):
    return self.__validation_function
    
  def get_input_value(self):
    return self.__input_value

  def process_input(self):
    if self.__input_value is not None:
      print(f"Processing input value: {self.__input_value}" )
    else:
      print("No input value to process")
    
class FeedbackInputHandler(UserInputHandler):
  def __init__(self, prompt):
    super().__init__(prompt)
    self.__feedback_parts = None
    
  def prompt_for_input(self):
    while True:
      userInput = input(self.get_prompt())
      if self.validate_Input(userInput):
        self.__feedback_parts = list(map(int, userInput.split()))
        return userInput
      else:
        print("Try again")

  def validate_Input(self, user_input):
    input_parts = user_input.split()
    #converts to integer
    if len(input_parts) == 3:
      try:
        #map applies int to each of the iterable input parts
        year, month, passengers = map(int, input_parts)
        year = int(year)
        month = int(month)
        passengers = int(passengers)
        if 1900 <= year <= 2023 and len(str(year)) == 4:
          return 1 <= month <= 12 and passengers >= 0
        else: 
          return False
      except ValueError:
        pass
      return False

    

    def get_year(self):
      return self.__feedback_parts[0] if self.__feedback else None

    def get_month(self):
      return self.feedback_parts[1] if self.__feedback else None


    def get_passengers(self):
      return self.feedback_parts[2] if self.__feedback else None

    
    def provide_feedback(self):
      if self.__feedback_parts is not None:
        print(f"Feedback: {self.__feedback_parts[0]} {self.__feedback_parts[1]} {self.__feedback_parts[2]}")
      else:
        print("No feedback provided")

    def get_feedback_parts(self):
      return self.__feedback_parts