from curses import window
import PySimpleGUI as sg
import json
import random

file = open("recipes.json")
data = json.load(file)

recipes = data["recipes"]
recipes_length = len(recipes)

filter_column = [
  [sg.Text('Available filters:', size=(240, 1))],
  [sg.HorizontalSeparator()],
  [sg.Button('Pick random recipe')]
  ]

result_column = [
  [sg.Text('Result:')],
  [sg.Text(key="result-name", size=(240, 1))],
  [sg.Text(key="result-source")]
]

layout = [[sg.Column(filter_column, size=(250, 500)), sg.VerticalSeparator(), sg.Column(result_column, size=(750, 500))]]

window = sg.Window('Recepy Picker', layout, size=(1000, 500))

while True:
  event, values = window.read()
  if event == 'Exit' or event == sg.WIN_CLOSED:
    break
  if event == 'Pick random recipe':
    result = data["recipes"][random.randint(0, recipes_length - 1)]
    window["result-name"].update(result["name"])
    window["result-source"].update(result["source"])
  
window.close()