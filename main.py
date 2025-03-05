# Анализ маржинальности
import pandas as pd
import numpy as np

df_income = pd.read_excel('доходы.xlsx')
df_expenses = pd.read_excel('расходы.xlsx')

def calculate_marginality(income, variable_expenses):
  total_income = 0
  total_variable_expenses = 0

  for i in income: # берёт каждое значение из столбца и складывает
   total_income += i
  for i, j in zip(df_expenses['Сумма'], df_expenses['Категория']): # берём для каждой строки значения обоих столбцов и делаем из них массив, и присваиваем i, j значения в массиве
   
   if j in ['Сырье и материалы', 'Зарплаты', 'Логистика']:

    total_variable_expenses += i
  print(f'Cумма переменных расходов равна: {total_variable_expenses}')
  print(f'Выручка равна: {total_income}')
  
  # Маржа = Выручка − Переменные расходы
  # Маржинальность = Маржа / Выручка × 100%
  margin = total_income - total_variable_expenses
  marginality = f'{round(margin / total_income * 100, 4)}%'
  print(f'Маржа: {margin}')
  print(f'Маржинальность: {marginality}')