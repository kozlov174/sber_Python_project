import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("sales.csv")  # пропуски обнаружены не были, поэтому чистить нечего
    summ = 0  # итоговая стоимость всех товаров
    phone_summ = 0  # итоговая выручка от телефонов
    for i in range(0, len(data)):
        summ = summ + data["Цена"].iloc[i] * data["Количество"].iloc[i]
        summ = round(summ, 2)
        if data["Продукт"].iloc[i] == "Телефон":
            phone_summ = phone_summ + data["Цена"].iloc[i] * data["Количество"].iloc[i]
        phone_summ = round(phone_summ, 2)
    print(summ)
    print(phone_summ)
