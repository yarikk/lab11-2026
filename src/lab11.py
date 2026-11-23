import pandas as pd

# Завантаження даних
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# Первинний аналіз даних
print("Перші 5 рядків:")
print(df.head())
print("\nЗагальна інформація:")
df.info()
print("\nСтатистичні характеристики:")
print(df.describe())

# Фільтрація даних (quantity більше середнього значення quantity по всьому DataFrame)
filtered_df = df[df['quantity'] > df['quantity'].mean()]
print("\nВідфільтровані дані (quantity > середнього):")
print(filtered_df)

# Сортування даних (за date та price у порядку спадання)
sorted_df = df.sort_values(by=['date', 'price'], ascending=[False, False])
print("\nВідсортовані дані:")
print(sorted_df)

# Групування та агрегування даних (мінімальна та максимальна ціна для кожного товару в магазині)
grouped_df = df.groupby(['store_id', 'product_id'])['price'].agg(['min', 'max']).reset_index()
print("\nЗгруповані дані (мінімальна та максимальна ціна):")
print(grouped_df)

# Додавання стовпця (день тижня, витягнутий з date)
df['day_of_week'] = df['date'].dt.day_name()
print("\nДані з новим стовпцем day_of_week:")
print(df)

# Видалення рядків (видалити всі рядки, де store_id дорівнює 3)
df_after_drop = df[df['store_id'] != 3].copy()
print("\nДані після видалення рядків зі store_id == 3:")
print(df_after_drop)

# Обробка пропущених значень (замінити NaN в price на середнє значення ціни для відповідного product_id)
df_after_drop['price'] = df_after_drop.groupby('product_id')['price'].transform(lambda x: x.fillna(x.mean()))
print("\nДані після заповнення пропущених значень в 'price':")
print(df_after_drop)

# Створення зведеної таблиці (рядки - store_id, стовпці - day_of_week, комірки - середнє quantity)
pivot_table = df_after_drop.pivot_table(values='quantity', index='store_id', columns='day_of_week', aggfunc='mean')
print("\nЗведена таблиця:")
print(pivot_table)
