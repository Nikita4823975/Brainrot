def calculate_marginality(income, variable_expenses):
  total_income = 0
  total_variable_expenses = 0

  for i in income: # берёт каждое значение из столбца и складывает
    total_income += i
  for i in variable_expenses:
    total_variable_expenses += i
  print(f'Cумма переменных расходов равна: {total_variable_expenses}')
  print(f'Выручка равна: {total_income}')
  
  # Маржа = Выручка − Переменные расходы
  # Маржинальность = Маржа / Выручка × 100%
  margin = total_income - total_variable_expenses
  marginality = f'{round(margin / total_income * 100, 4)}%'
  print(f'Маржа: {margin}')
  print(f'Маржинальность: {marginality}')

def main():
  # Анализ маржинальности
  import pandas as pd
  import numpy as np

  df_income = pd.read_excel('доходы.xlsx')
  df_expenses = pd.read_excel('расходы.xlsx')
  # фильтруем все расходы, оставляя только переменные расходы
  df_expenses = df_expenses[df_expenses['Категория'].isin(['Сырье и материалы', 'Зарплаты', 'Логистика'])]
  calculate_marginality(df_income['Сумма'], df_expenses['Сумма'])

if __name__ == "__main__":
    main()