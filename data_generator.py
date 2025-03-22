import pandas as pd
import numpy as np
import random

# Настройки генерации
np.random.seed(42)
random.seed(42)
NUM_ROWS = 1000

# Категории доходов с весами и диапазонами (в рублях)
income_categories = {
    'Азотные удобрения': {'weight': 20, 'min': 50000, 'max': 200000},
    'Фосфорные удобрения': {'weight': 15, 'min': 40000, 'max': 180000},
    'Калийные удобрения': {'weight': 25, 'min': 60000, 'max': 220000},
    'Комплексные удобрения': {'weight': 30, 'min': 100000, 'max': 300000},
    'Органические удобрения': {'weight': 10, 'min': 30000, 'max': 150000}
}

# Категории расходов с весами и диапазонами (в рублях)
expense_categories = {
    'Сырье и материалы': {'weight': 35, 'min': 100000, 'max': 500000},
    'Зарплаты': {'weight': 25, 'min': 200000, 'max': 400000},
    'Логистика': {'weight': 20, 'min': 50000, 'max': 150000},
    'Энергетика': {'weight': 15, 'min': 80000, 'max': 200000},
    'Обслуживание': {'weight': 5, 'min': 30000, 'max': 100000}
}

expense_subcategories = [
    'Азотные удобрения',
    'Фосфорные удобрения',
    'Калийные удобрения',
    'Комплексные удобрения',
    'Органические удобрения'
]

def generate_data(categories_dict, subcategories, num_rows):
    # Нормализация весов
    total_weight = sum(cat['weight'] for cat in categories_dict.values())
    probabilities = [cat['weight']/total_weight for cat in categories_dict.values()]
    
    # Генерация категорий
    cats = np.random.choice(
        list(categories_dict.keys()),
        size=num_rows,
        p=probabilities
    )

    # Генерация подкатегорий
    if subcategories:
        subcats = np.random.choice(
            subcategories,
            size=num_rows
        )
    else:
        subcats = cats

    # Генерация временных меток (месяц, год)
    months = []
    years = []

    cur_month = 0
    prev_cats = []
    for cat, subcat in zip(cats, subcats):
        if [cat, subcat] in prev_cats or random.random() <.5:
            cur_month += 1
            prev_cats = []
        else:
            prev_cats.append([cat, subcat])

        months.append(1+cur_month%12)
        years.append(2000+cur_month//12)
    
    # Генерация сумм
    amounts = [
        random.randint(
            categories_dict[cat]['min'],
            categories_dict[cat]['max']
        ) for cat in cats
    ]

    if subcategories:
        return pd.DataFrame({
            'Сумма': amounts,
            'Категория': cats,
            'Подкатегория': subcats,
            'Месяц': months,
            'Год': years
        })
    else:
        return pd.DataFrame({
            'Сумма': amounts,
            'Категория': cats,
            'Месяц': months,
            'Год': years
        })

# Генерация данных
df_income = generate_data(income_categories, None, NUM_ROWS)
df_expense = generate_data(expense_categories, expense_subcategories, NUM_ROWS)

print(df_income)
print(df_expense)

# Сохранение в разные файлы
df_income.to_excel('доходы.xlsx', sheet_name='Доходы', index=False)
df_expense.to_excel('расходы.xlsx', sheet_name='Расходы', index=False)
