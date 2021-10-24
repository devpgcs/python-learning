import utils

history = []
previous_results = []


def should_calculate(operation):
  current_operation = utils.operations[operation][0]
  current_operation_symbol = utils.operations[operation][1]
  user_wants_to_use_previous_result = utils.ask_to_use_previous_result(previous_results)

  if user_wants_to_use_previous_result:
    number_one = previous_results[-1]
  else:
    number_one = input(f"Enter the first number to {current_operation}: ").lstrip()

  number_two = input(f"Enter the second number to {current_operation}: ").lstrip()
  
  # Make the calculation depending of the `operation` index
  if operation == 0:
    result = float(number_one) + float(number_two)
  elif operation == 1:
    result = ((float(number_one) * 100) - (float(number_two) * 100)) / 100
  elif operation == 2:
    result = float(number_one) * float(number_two)
  elif operation == 3:
    result = float(number_one) / float(number_two)

  # We need to add every calculation to the history list, and display in a readable way 
  result_string = f"{number_one} {current_operation_symbol} {number_two} = {result}"
  history.append(result_string)

  # Also, we need to apend the current result to the `previous_results` list
  # since we gonna ask to the users if they wants to use the previous value
  # on next calculations.
  previous_results.append(result)

  utils.print_result_interface(result_string)


def handle_user_decision(decision):
  try:
    int(decision)
  except:
    return utils.print_error_interface()

  if int(decision) in range(1,4):
    should_calculate(int(decision) - 1)
  
  if decision == "5":
    utils.print_history_interface(history)

  if decision == "6":
    utils.print_good_bye_interface()

while True:
  print("What do you want to do?")
  print("1. Sum")
  print("2. Substract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Show history")

  print("\n6. Close calculator")

  user_choice = input("Enter a number from the list: ").lstrip()

  handle_user_decision(user_choice)