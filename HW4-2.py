import numpy as np
import pandas as pd

if __name__ == '__main__':
    df11 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                        'weight': ['high', 'medium', 'low'] * 3,
                        'price': np.random.randint(0, 15, 9)})

    df21 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                        'kilo': ['high', 'low'] * 3,
                        'price': np.random.randint(0, 15, 6)})

    # 2.2
    df12 = pd.DataFrame({'fruit': ['apple', 'orange', 'banana'] * 3,
                        'weight': ['high', 'medium', 'low'] * 3,
                        'price': np.arange(9)})

    df22 = pd.DataFrame({'fruit': ['apple', 'orange', 'pine'] * 2,
                        'weight': ['high', 'medium'] * 3,
                        'price': np.arange(6)})


    #задание 1

    merged_df = df11.merge(df21, left_on=['fruit', 'weight'], right_on=['pazham', 'kilo'], how='inner')
    print(merged_df)

    #задание 2

    merged = df12.merge(df22, on=['fruit', 'weight', 'price'], how='left', indicator=True)
    #Благодаря интернету найден параметр insicator, который позволяет помечать одинаковые значения
    merged = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])
    print(merged)