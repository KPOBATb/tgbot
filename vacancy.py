import pandas as pd 

df= pd.read_excel("Вакансии для бота.xlsx","Лист1")
df_id= pd.read_excel("Вакансии для бота.xlsx","Лист2")

def vacancy_name(subject,city,type,df=df):
    return df[(df['Субъект федерации']==subject) & (df['Город']==city) & (df['Специализация']==type)]['Название должности'].values
# print(vacancy_name('Хабаровский край','Амурск','Рабочие'))

def vacany_id(name,df=df_id):
    return df[df['вакансия']==name]["id _vacanacy"].values[0]
# print(vacany_id('Электромонтер по обслуживанию и ремонту устройств сигнализации, централизации и блокировки'))

def vacanacy_vacanacy(id,df=df_id):
    return df[df['id _vacanacy']==int(id)]["вакансия"].values[0]

# print(vacanacy_vacanacy("1"))
# print(vacanacy_vacanacy(1))


def vacancy_show(subject,city,type,name,df=df):
    return df[(df['Субъект федерации']==subject) & (df['Город']==city) & (df['Специализация']==type) & (df['Название должности']==name)]
#['Название должности', 'Обязанности', 'Требования', 'Опыт работы', 'Условия работы', 'Доход по должности', 'Специализация', 'Субъект федерации', 'Город', 'График работы', 'Ответственное контактное лицо по заявке', 'Адрес электронной почты', 'Контактный телефон', 'Ссылка на Telegram']
# print(vacancy_show('Хабаровский край','Амурск','Рабочие','Электромонтер по обслуживанию и ремонту устройств сигнализации, централизации и блокировки').to_dict().keys())

df= pd.read_excel("Вакансии для бота.xlsx","Лист5")
# print(df)
def vacancies_by_city(df=df):
    subject={i:set() for i in df['Субъект федерации'].unique()}
    for i in df['Субъект федерации'].unique():
        for j in df[df['Субъект федерации']==i]['Город'].unique():
            subject[i].add(j)
    return subject
# print(vacancies_by_city())
city={'Хабаровский край': {'Амурск'}, 'Приморский край': {'Пограничный'}, 'Амурская область': {'Благовещенск', 'Магдагачи'}}
# print(city['Хабаровский край'])

def vacancy_cool(df):
    keys = ['Название должности', 'Обязанности', 'Требования', 'Опыт работы', 'Условия работы', 'Доход по должности', 'Специализация', 'Субъект федерации', 'Город', 'График работы', 'Ответственное контактное лицо по заявке', 'Адрес электронной почты', 'Контактный телефон', 'Ссылка на Telegram']
    output=[]
    for i in keys:
        output.append(df[i].values[0])
    output = {keys[i]:output[i] for i in range(len(keys))}
    vacancy = output
    output = "Вакансия:\n"
    output += vacancy['Название должности'] + "\n\n"
    output += "1. Обязанности:\n"
    for i in range(len(vacancy['Обязанности'].split(';'))):
        string = str(vacancy['Обязанности'].split(';')[i]).strip()
        output += string + "\n"
    output += "\n"
    output += "2. Требования:\n"
    for i in range(len(vacancy['Требования'].split(';'))):
        string = str(vacancy['Требования'].split(';')[i]).strip()
        output += string + "\n"
    output += "\n"
    output += "3. Опыт работы:\n"
    output += vacancy['Опыт работы'] + "\n\n"
    output += "4. Условия:\n"
    for i in range(len(vacancy['Условия работы'].split(';'))):
        string = str(vacancy['Условия работы'].split(';')[i]).strip()
        output += string + "\n"
    output += "\n"
    output += "5. Доход по должности:\n"
    output += str(vacancy['Доход по должности']).replace('00000','00 000').replace('0000','0 000') + "\n\n"
    output += "6. Направление деятельности:\n"
    output += vacancy['Специализация'] + "\n\n"
    output += "7. График работы:\n"
    output += vacancy['График работы'] + "\n\n"
    output += "8. Субъект федерации:\n"
    output += vacancy['Субъект федерации'] + "\n\n"
    output += "9. Ответственное контактное лицо по заявке:\n"
    output += vacancy['Ответственное контактное лицо по заявке'] + "\n\n"
    output += "10. Адрес электронной почты:\n"
    output += vacancy['Адрес электронной почты'] + "\n\n"
    output += "11. Контактный телефон:\n"
    output += vacancy['Контактный телефон'].replace(" ","") + "\n\n"
    output += "12. Ссылка на Telegram:\n"
    output += vacancy['Ссылка на Telegram']
    return output

# print(vacancy_cool(vacancy_show('Хабаровский край','Амурск','Рабочие','Электромонтер по обслуживанию и ремонту устройств сигнализации, централизации и блокировки')))