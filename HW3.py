import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('HW3_pandas.csv')

    #Выведем всех студентов, которые живут в Екатеринбурге и их баллы свыше 70
    filtered_students = data[(data["Город"] == "Екатеринбург") & (data["Баллы"] > 70)]
    print(filtered_students)

    #Выставление оценок на основе баллов студента по системе БРС УрФУ
    #Также внутри цикла реализована замена пустых значений на 45
    data["Оценка"] = 0
    for i in range(0, len(data["Имя"])):
        if pd.isna(data["Баллы"].iloc[i]):
            data["Баллы"].iloc[i] = 45
        if data["Баллы"].iloc[i] >= 80:
            data["Оценка"].iloc[i] = 5
        elif (data["Баллы"].iloc[i] >= 60) and (data["Баллы"].iloc[i] < 80):
            data["Оценка"].iloc[i] = 4
        elif (data["Баллы"].iloc[i] >= 40) and (data["Баллы"].iloc[i] < 60):
            data["Оценка"].iloc[i] = 3
        else:
            data["Оценка"].iloc[i] = 2

    #Построние графика распределения оценок среди студентов и графика нахождения студентов
    plt.figure(figsize=(8, 5))
    data["Оценка"].value_counts().plot(kind='bar')
    plt.show()
    plt.figure(figsize=(8, 5))
    data["Город"].value_counts().plot(kind='bar')
    plt.show()

    #На основе изученных данных можно сделать вывод, что самое большое количество студентов из Екатеринбурга
    #А также большая часть из них закрыла предмет на положительные оценки(5 и 4)
