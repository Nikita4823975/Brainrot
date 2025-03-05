# Анализ маржинальности
import pandas as pd
import numpy as np

df_income = pd.read_excel('доходы.xlsx')
df_expense = pd.read_excel('расходы.xlsx')
total_income = 0
total_expense = 0

for i in df_income['Сумма']: # берёт каждое значение из столбца и складывает
  total_income += i
print(f'Полная сумма доходов равна: {total_income}')

for i, j in zip(df_expense['Сумма'], df_expense['Категория']): # берём для каждой строки значения обоих столбцов и делаем из них массив, и присваиваем i, j значения в массиве
  if j in ['Сырье и материалы', 'Зарплаты', 'Логистика']:
    total_expense += i
print(f'Полная сумма переменных расходов равна: {total_expense}')