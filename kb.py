from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import pandas as pd
import numpy as np
from vacancy import vacanacy_vacanacy

df = pd.read_excel("Вакансии для бота.xlsx","Лист3")
df_city= pd.read_excel("Вакансии для бота.xlsx","Лист4")
df_resume= pd.read_excel("resume.xlsx","Лист1")
df_resume1 =pd.read_excel("resume1.xlsx","Лист1")
MenuKeybord = InlineKeyboardBuilder()
MenuKeybord.add(types.InlineKeyboardButton(
        text="Ищу вакансию",
        callback_data="need_vacancy"))
MenuKeybord.add(types.InlineKeyboardButton(
        text="Ищу работника",
        callback_data="need_worker"))
MenuKeybord.add(types.InlineKeyboardButton(
        text="Загрузить резюме",
        callback_data="load_resume"))
MenuKeybord.adjust(1)


#vacancy_typeKeybord - v_t_
#selected_city - s_c_

Subject_of_rfKeybord = InlineKeyboardBuilder()
for i in df["Субъект федерации"].unique():
        Subject_of_rfKeybord.add(types.InlineKeyboardButton( text=i, callback_data=f"s_of_rf_{i}"))
Subject_of_rfKeybord.adjust(1)

# CityKeybord = InlineKeyboardBuilder()
# for i in df_city["Город"].unique():
#     CityKeybord.add(types.InlineKeyboardButton(text=f"{i}",
#     callback_data=f"s_c_{i}"))
# CityKeybord.adjust(2)

vacancy_typeKeybord = InlineKeyboardBuilder()
vacancy_typeKeybord.add(types.InlineKeyboardButton(
        text="Рабочие",
        callback_data="v_t_Рабочие"))
vacancy_typeKeybord.add(types.InlineKeyboardButton(
        text="Руководители",
        callback_data="v_t_chief"))
vacancy_typeKeybord.add(types.InlineKeyboardButton(
        text="Специалисты",
        callback_data="v_t_specialist"))
vacancy_typeKeybord.adjust(2, 2)

#need_worker

Need_worker_subjectKeybord = InlineKeyboardBuilder()
# for i in df_resume[['Субъект федерации', 'Город']]:
for index, row in df_resume1.drop_duplicates(keep=False,subset=['Субъект федерации']).iterrows():
    id = row['id']
    text = row['Субъект федерации']
    Need_worker_subjectKeybord.add(types.InlineKeyboardButton( text=f"{text}", callback_data=f"n_w_s_of_rf_{id}"))
Need_worker_subjectKeybord.adjust(1)

GoBackKeybord = InlineKeyboardBuilder()
GoBackKeybord.add(types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="menu"))

YesNoKeybord = InlineKeyboardBuilder()
YesNoKeybord.add(types.InlineKeyboardButton(text="Да", callback_data="yes"))
YesNoKeybord.add(types.InlineKeyboardButton(text="Нет", callback_data="need_worker"))
YesNoKeybord.adjust(2)

DownloadConfirmationKeybord = InlineKeyboardBuilder()
DownloadConfirmationKeybord.add(types.InlineKeyboardButton( text="Да",callback_data="DownloadConfirmationyes"))
DownloadConfirmationKeybord.add(types.InlineKeyboardButton(text="Нет",callback_data="DownloadConfirmationno"))
DownloadConfirmationKeybord.adjust(2)


# print(df_resume1.drop_duplicates(keep=False,subset=['Субъект федерации']).iterrows())
