def calculate_marginality(income, variable_expenses):
    # Функция для общего расчёта маржинальности у всех категорий и дат
    # ввод: массив с доходами [int], массив с расходами [int]
    # вывод: маржа int, маржинальность string
    total_income = 0
    total_variable_expenses = 0

    for i in income:  # берёт каждое значение из столбца и складывает
        total_income += i
    for i in variable_expenses:
        total_variable_expenses += i
    print(f'Cумма переменных расходов равна: {total_variable_expenses}')
    print(f'Выручка равна: {total_income}')

    # Маржа = Выручка − Переменные расходы
    # Маржинальность = Маржа / Выручка × 100%
    margin = total_income - total_variable_expenses
    marginality = f'{round(margin / total_income * 100, 4)}%'  # 4 цифры после запятой

    return margin, marginality


def main():
    # Анализ маржинальности
    import pandas as pd
    import numpy as np

    df_income = pd.read_excel('доходы.xlsx')
    df_expenses = pd.read_excel('расходы.xlsx')
    # фильтруем все расходы, оставляя только переменные расходы
    df_expenses = df_expenses[df_expenses['Категория'].isin(['Сырье и материалы', 'Зарплаты', 'Логистика'])]

    # Общая маржинальность
    margin, marginality = calculate_marginality(df_income['Сумма'], df_expenses['Сумма'])
    print(f'Маржа: {margin}')
    print(f'Маржинальность: {marginality}')

    # Категориальная маржинальность
    categories = ['Азотные удобрения', 'Фосфорные удобрения']
    df_income_categorical = df_income[df_income['Категория'].isin(categories)]
    df_expenses_categorical = df_expenses[df_expenses['Подкатегория'].isin(categories)]
    margin, marginality = calculate_marginality(df_income_categorical['Сумма'], df_expenses_categorical['Сумма'])
    print(f'Маржа в категориях {categories}: {margin}')
    print(f'Маржинальность в категориях {categories}: {marginality}')

    # Маржинальность по датам
    year = [2000]
    month = [1]
    df_income_dated = df_income[((df_income['Месяц'].isin(month)) & (df_income['Год'].isin(year)))]
    df_expenses_dated = df_expenses[((df_expenses['Месяц'].isin(month)) & (df_expenses['Год'].isin(year)))]
    margin, marginality = calculate_marginality(df_income_dated['Сумма'], df_expenses_dated['Сумма'])
    print(f'Маржа в дате {month, year}: {margin}')
    print(f'Маржинальность в дате {month, year}: {marginality}')


if __name__ == "__main__":
    main()
