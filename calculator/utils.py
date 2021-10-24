border = "=" * 100
operations = [["sum", "+"], ["substract", "-"], ["multiply", "*"], ["divide", "/"]]


def ask_to_use_previous_result(previous_results):
  has_previous_results = len(previous_results) > 0
  user_wants_to_use_previous_value = False

  if has_previous_results:
    # We must ask to the users if they wants to use the previous result and they
    # must provide a Y or N answer. Otherwise we should ask again and again.
    question_value = None

    while (question_value != "Y" and question_value != "y" and question_value != "N" and question_value != "n"):
      question_string = f"You would like to use the previous result {previous_results[-1]}? Y/N: "
      question_value = input(question_string)

    # Once we have a right answer from the users, we only must set the True decision since
    # we already initialize the `user_wants_to_use_previous_value` as False and is not necessary
    # to update the `user_wants_to_use_previous_value` with the same value.
    if question_value == "Y" or question_value == "y":
      user_wants_to_use_previous_value = True

  return user_wants_to_use_previous_value


def print_result_interface(result):
  print(border)
  print("\t RESULT: ", result)
  print(border)


def print_history_interface(history):
  has_history = len(history) > 0

  print(border)
  print("CALCULATOR HISTORY")

  if has_history:
    for index in range(len(history)):
      list_position = index + 1
      list_item = history[index]

      formatted_item = f"{list_position}.\t{list_item}"

      print(formatted_item)
  else:
    print("\tYou have not history")

  print(border)


def print_error_interface():
  print(border)
  print("\tERROR: You should provide a number between 1 and 6 to proceed")
  print(border)


def print_good_bye_interface():
  print(border)
  print("Good bye and have a nice day!")
  print(border)
  exit()