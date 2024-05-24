import tkinter as tk  #GUI
from tkinter import ttk  # allows for tabs
import math  # math
import numpy as np  # trig and graphing
from sympy import *  # graphing
from sympy.abc import x # graphing
from sympy.solvers import solve # scientific math functions
from sympy.plotting import plot # graphing
import matplotlib.pyplot as plt # graphing

mainWindow = tk.Tk() # initializes graphing calculator 



# This section of code was sourced from GeeksforGeeks
# https://www.geeksforgeeks.org/quick-way-check-characters-string/
def allCharactersSame(s):
  return all(c == s[0] for c in s)
# checks how many graphing equations are blank, this is because sympy cannot graph blank functions
# end section

# # scientific calculator

calculator = ttk.Notebook(mainWindow) # enables tabbed windows for science and graphing calculators.

science = ttk.Frame(calculator) # scientific tab
graphing = ttk.Frame(calculator) # graphing tab

calculator.add(science, text="Scientific") # adds the two tabs to the main calculator window
calculator.add(graphing, text="Graphing")

mainLabel = tk.Label(science) # shows entry of equations into scientific calculator 
mainLabel.grid(row=0, column=2)


def cycle(n): # this procedure cycles through the three fields enabled for the graphing calculator
  if n['text'] == "selected equation: y1":
    n.config(text="selected equation: y2")
  elif n['text'] == "selected equation: y2":
    n.config(text="selected equation: y3")
  elif n['text'] == "selected equation: y3":
    n.config(text="selected equation: y1")

def graph(n1, n2, n3):
  parameters_list = [n1['text'],n2['text'],n3['text']]
  print(parameters_list)
  x_range_lower = float(input("Set the lower x-boundary...."))
  x_range_upper = float(input("Set the upper x-boundary...."))
  y_range_lower = float(input("Set the lower y boundary...."))
  y_range_upper = float(input("Set the upper y-boundary...."))

  # graphing_expression is entered into the graph software to
  # allow Sympy to graph the function
  # graphing_equation includes y1 = and cannot be used to graph   
  # with Sympy.

  plt.rcParams['figure.figsize'] = 3, 3
  for n in range(3):
    name = "y" + str(n) 
    parameters_list[n] = parameters_list[n][6:len(parameters_list[n])]
  for n in reversed(range(3)):
    if allCharactersSame(parameters_list[n]):
      print(len(parameters_list))
      parameters_list.remove(parameters_list[n])
  print(parameters_list)
  # checks how many are blank, this is because sympy cannot graph blank functions

  # this section of code checks to see how many graphing equations are blank and graphs the ones that aren't.
  
 # if not allCharactersSame(graphing_expression_1) and not allCharactersSame(
 
  p1 = plot(parameters_list, show=false, ylim=[y_range_lower, y_range_upper], xlim=[x_range_lower, x_range_upper])
  p1.show()
# end section

def sqrt():
  mainLabel_current_text = mainLabel['text']
  eval_result = eval(str(mainLabel_current_text)) # evaulates the current entry before it is taken to the 1/2 power
  mainLabel_new_text = math.pow(eval_result, 0.5)
  mainLabel.config(text=mainLabel_new_text)


def clear():
  mainLabel_new_text = ""
  mainLabel.config(text=mainLabel_new_text)


def eval_function(): # evaluates expressions
  try:
    mainLabel_current_text = mainLabel['text']
    if "np.sin(math.pi)" in mainLabel_current_text or "np.tan(math.pi)" in mainLabel_current_text:
      mainLabel.config(text=0) # allows for calculator to properly evaulate certain trig functions
    else:
      mainLabel_new_text = eval(mainLabel_current_text)
      mainLabel.config(text=mainLabel_new_text)

  except: # provides for an error whenever extra characters were added
    mainLabel_new_text = "ERROR" 
    mainLabel.config(text=mainLabel_new_text)


def append_graphing(n): # This allows for cycling through fields to graph the equation
  # if selected equation = y1
  if selected_equation['text'] == "selected equation: y1":
    graph_equation_1_currentText = graph_equation_1['text']
    graph_equation_1_newText = str(graph_equation_1_currentText) + str(n)
    graph_equation_1.config(text=graph_equation_1_newText)
  # if selected equation = y2
  if selected_equation['text'] == "selected equation: y2":
    graph_equation_2_currentText = graph_equation_2['text']
    graph_equation_2_newText = str(graph_equation_2_currentText) + str(n)
    graph_equation_2.config(text=graph_equation_2_newText)
  # if selected equation = y3
  if selected_equation['text'] == "selected equation: y3":
    graph_equation_3_currentText = graph_equation_3['text']
    graph_equation_3_newText = str(graph_equation_3_currentText) + str(n)
    graph_equation_3.config(text=graph_equation_3_newText)


def clear_graphing(): # this clears whatever field is selected through the cycle procedure
  # clear y1
  if selected_equation['text'] == "selected equation: y1":
    graph_equation_1_newText = "y1 = "
    graph_equation_1.config(text=graph_equation_1_newText)
  # clear y2
  if selected_equation['text'] == "selected equation: y2":
    graph_equation_2_newText = "y2 = "
    graph_equation_2.config(text=graph_equation_2_newText)
  # clear y3
  if selected_equation['text'] == "selected equation: y3":
    graph_equation_3_newText = "y3 = "
    graph_equation_3.config(text=graph_equation_3_newText)


def append(n): # adds new entries to scientific text
  mainLabel_current_text = mainLabel['text']
  mainLabel_new_text = str(mainLabel_current_text) + str(n)
  mainLabel.config(text=mainLabel_new_text)


def main():

  # all buttons - graphing
  button_number_one_science = tk.Button(science,
                                        text=1,
                                        command=lambda: append(1))
  button_number_one_science.grid(row=1, column=1)
  button_number_two_science = tk.Button(science,
                                        text=2,
                                        command=lambda: append(2))
  button_number_two_science.grid(row=1, column=2)
  button_number_three_science = tk.Button(science,
                                          text=3,
                                          command=lambda: append(3))
  button_number_three_science.grid(row=1, column=3)
  button_number_four_science = tk.Button(science,
                                         text=4,
                                         command=lambda: append(4))
  button_number_four_science.grid(row=2, column=1)
  button_number_five_science = tk.Button(science,
                                         text=5,
                                         command=lambda: append(5))
  button_number_five_science.grid(row=2, column=2)
  button_number_six_science = tk.Button(science,
                                        text=6,
                                        command=lambda: append(6))
  button_number_six_science.grid(row=2, column=3)
  button_number_seven_science = tk.Button(science,
                                          text=7,
                                          command=lambda: append(7))
  button_number_seven_science.grid(row=3, column=1)
  button_number_eight_science = tk.Button(science,
                                          text=8,
                                          command=lambda: append(8))
  button_number_eight_science.grid(row=3, column=2)
  button_number_nine_science = tk.Button(science,
                                         text=9,
                                         command=lambda: append(9))
  button_number_nine_science.grid(row=3, column=3)
  button_number_zero_science = tk.Button(science,
                                         text=0,
                                         command=lambda: append(0))
  button_number_zero_science.grid(row=4, column=2)

  # addition, subtraction, multiplication, division
  button_addition_science = tk.Button(science,
                                      text="+",
                                      command=lambda: append("+"))
  button_addition_science.grid(row=1, column=4)

  button_subtraction_science = tk.Button(science,
                                         text="-",
                                         command=lambda: append("-"))
  button_subtraction_science.grid(row=2, column=4)

  button_multiplication_science = tk.Button(science,
                                            text="*",
                                            command=lambda: append("*"))
  button_multiplication_science.grid(row=3, column=4)

  button_division_science = tk.Button(science,
                                      text="/",
                                      command=lambda: append("/"))
  button_division_science.grid(row=4, column=4)

  # equal button
  button_equal_science = tk.Button(science, text="=", command=eval_function)
  button_equal_science.grid(row=4, column=3)

  # CLR button
  button_clear_science = tk.Button(science, text="CLR", command=clear)
  button_clear_science.grid(row=4, column=1)

  # exponentiation
  button_exponent_science = tk.Button(science,
                                      text='x\u207f',
                                      command=lambda: append("**"))
  button_exponent_science.grid(row=1, column=5)

  # square roots
  button_root_science = tk.Button(science, text="√", command=sqrt)
  button_root_science.grid(row=2, column=5)
  # trigonometric functions
  button_sin_science = tk.Button(science,
                                 text="sin()",
                                 command=lambda: append("np.sin("))
  button_sin_science.grid(row=1, column=6)
  button_cos_science = tk.Button(science,
                                 text="cos()",
                                 command=lambda: append("np.cos("))
  button_cos_science.grid(row=2, column=6)
  button_tan_science = tk.Button(science,
                                 text="tan()",
                                 command=lambda: append("np.tan("))
  button_tan_science.grid(row=3, column=6)
  # parenthesis
  button_left_parenthesis_science = tk.Button(science,
                                              text="(",
                                              command=lambda: append("("))
  button_left_parenthesis_science.grid(row=3, column=5)
  button_right_parenthesis_science = tk.Button(science,
                                               text=")",
                                               command=lambda: append(")"))
  button_right_parenthesis_science.grid(row=4, column=5)
  button_pi_science = tk.Button(science,
                                text="π",
                                command=lambda: append("math.pi"))
  button_pi_science.grid(row=4, column=6)
  button_decimal_science = tk.Button(science,
                                     text=".",
                                     command=lambda: append("."))
  button_decimal_science.grid(row=4, column=7)

  # graphing
  global selected_equation
  selected_equation = tk.Label(graphing, text="selected equation: y1")
  selected_equation.grid(row=0, column=0)
  global graph_equation_1
  graph_equation_1 = tk.Label(graphing, text="y1 =  ")
  global graph_equation_2
  graph_equation_2 = tk.Label(graphing, text="y2 =  ")
  global graph_equation_3
  graph_equation_3 = tk.Label(graphing, text="y3 =  ")
  graph_equation_1.grid(row=1, column=0)
  graph_equation_2.grid(row=2, column=0)
  graph_equation_3.grid(row=3, column=0)

  # buttons 0 - 9
  button_number_one = tk.Button(graphing,
                                text=1,
                                command=lambda: append_graphing(1))
  button_number_one.grid(row=5, column=1)
  button_number_two = tk.Button(graphing,
                                text=2,
                                command=lambda: append_graphing(2))
  button_number_two.grid(row=5, column=2)
  button_number_three = tk.Button(graphing,
                                  text=3,
                                  command=lambda: append_graphing(3))
  button_number_three.grid(row=5, column=3)
  button_number_four = tk.Button(graphing,
                                 text=4,
                                 command=lambda: append_graphing(4))
  button_number_four.grid(row=6, column=1)
  button_number_five = tk.Button(graphing,
                                 text=5,
                                 command=lambda: append_graphing(5))
  button_number_five.grid(row=6, column=2)
  button_number_six = tk.Button(graphing, text=6, command=lambda: append(6))
  button_number_six.grid(row=6, column=3)
  button_number_seven = tk.Button(graphing,
                                  text=7,
                                  command=lambda: append_graphing(7))
  button_number_seven.grid(row=7, column=1)
  button_number_eight = tk.Button(graphing,
                                  text=8,
                                  command=lambda: append_graphing(8))
  button_number_eight.grid(row=7, column=2)
  button_number_nine = tk.Button(graphing,
                                 text=9,
                                 command=lambda: append_graphing(9))
  button_number_nine.grid(row=7, column=3)
  button_number_zero = tk.Button(graphing,
                                 text=0,
                                 command=lambda: append_graphing(0))
  button_number_zero.grid(row=8, column=2)

  # addition, subtraction, multiplication, division
  button_addition = tk.Button(graphing,
                              text="+",
                              command=lambda: append_graphing("+"))
  button_addition.grid(row=5, column=4)

  button_subtraction = tk.Button(graphing,
                                 text="-",
                                 command=lambda: append_graphing("-"))
  button_subtraction.grid(row=6, column=4)

  button_multiplication = tk.Button(graphing,
                                    text="*",
                                    command=lambda: append_graphing("*"))
  button_multiplication.grid(row=7, column=4)

  button_division = tk.Button(graphing,
                              text="/",
                              command=lambda: append_graphing("/"))
  button_division.grid(row=8, column=4)

  # clear button
  button_clear = tk.Button(graphing, text="CLR", command=clear_graphing)
  button_clear.grid(row=8, column=1)
  # variable button
  button_variable = tk.Button(graphing,
                              text="X,T,θ,n",
                              command=lambda: append_graphing("x"))
  button_variable.grid(row=8, column=3)

  # exponentiation
  button_exponent = tk.Button(graphing,
                              text='x\u207f',
                              command=lambda: append_graphing("**"))
  button_exponent.grid(row=5, column=5)

  # square roots
  button_root = tk.Button(graphing,
                          text="√",
                          command=lambda: append_graphing("sqrt("))
  button_root.grid(row=6, column=5)

  # paretheses
  button_left_parenthesis = tk.Button(graphing,
                                      text="(",
                                      command=lambda: append_graphing("("))
  button_left_parenthesis.grid(row=7, column=5)
  button_right_parenthesis = tk.Button(graphing,
                                       text=")",
                                       command=lambda: append_graphing(")"))
  button_right_parenthesis.grid(row=8, column=5)

  # graph button
  button_graph = tk.Button(
    graphing,
    text="GRAPH",
    command=lambda: graph(graph_equation_1, graph_equation_2, graph_equation_3))
  button_graph.grid(row=4, column=6)

  # cycle button
  button_cycle = tk.Button(graphing,
                           text="CYCLE",
                           command=lambda: cycle(selected_equation))
  button_cycle.grid(row=5, column=6)
  button_sin = tk.Button(graphing,
                         text="sin()",
                         command=lambda: append_graphing("sin("))
  button_sin.grid(row=6, column=6)
  button_cos = tk.Button(graphing,
                         text="cos()",
                         command=lambda: append_graphing("cos("))
  button_cos.grid(row=7, column=6)
  button_tan = tk.Button(graphing,
                         text="tan()",
                         command=lambda: append_graphing("tan("))
  button_tan.grid(row=8, column=6)
  button_abs = tk.Button(graphing,
                         text="|x|",
                         command=lambda: append_graphing("abs("))
  button_abs.grid(row=5, column=7)
  button_decimal = tk.Button(graphing,
                             text=".",
                             command=lambda: append_graphing("."))
  button_decimal.grid(row=6, column=7)
  ###
  calculator.pack()
  # loops program window
  mainWindow.mainloop()


main()
