from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Filter
from aiogram.filters import Command
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram import Bot
from aiogram.types.input_file import FSInputFile

import fnmatch

import os

from vacancy import vacancy_show,vacancy_name,vacany_id,vacanacy_vacanacy,city,vacancy_cool
from resume import resume_add,resume_show,n_w_city,resume_sub_id,resume_show_2
from kb import MenuKeybord,Subject_of_rfKeybord,vacancy_typeKeybord,YesNoKeybord,GoBackKeybord,DownloadConfirmationKeybord,Need_worker_subjectKeybord
#,CityKeybord

# from vacancy import vacancies_by_city,shosen_vacancy_vy_id,vokancy_by_id
#s_of_rf_ субъект
#s_c_ город
#v_t_ тип
#c_v_ выбранная вакансия 

class Choice:
    def __init__(self):
        self.choice = {}
    def ap(self,key,key_two,value):
        if key not in self.choice:
            self.choice[key]={}
            self.choice[key][key_two]=value
        if key in self.choice:
            self.choice[key][key_two]=value
    def show(self,key):
        return self.choice[key]
    def clear(self,key):
        self.choice[key]={}

class Form(StatesGroup):
    file1 = State()
    file2 = State()
    file3 = State()
    file4 = State()
    fileload = State()

router = Router()
ch=Choice()
ch_resume=Choice()



@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer('Приветствую😊 \nЯ - бот по поиску работы компании ОАО «РЖД» - самого крупного работодателя страны! \n ',reply_markup=MenuKeybord.as_markup())

@router.callback_query(lambda query: query.data == "menu")
async def callback_data_handler(callback_query: CallbackQuery):
        await callback_query.bot.send_message(callback_query.from_user.id,'Приветствую😊 \nЯ - бот по поиску работы компании ОАО «РЖД» - самого крупного работодателя страны!',reply_markup=MenuKeybord.as_markup() )

#Need vacancy
#выбор субъекта 
@router.callback_query(lambda query: query.data == "need_vacancy")
async def callback_data_handler(callback_query: CallbackQuery):
        await callback_query.bot.send_message(callback_query.from_user.id,'Скажите, в каком субъекте РФ Вас интересуют вакансии?',reply_markup=Subject_of_rfKeybord.as_markup() )
#выбор города 
@router.callback_query(lambda query: query.data[0:len('s_of_rf_')] == "s_of_rf_")
async def callback_data_handler(callback_query: CallbackQuery):
        ch.ap(callback_query.from_user.id,'s_of_rf_',callback_query.data[len(callback_query.data)-callback_query.data[::-1].index("_"):])
        CityKeybord = InlineKeyboardBuilder()
        for i in city[ch.show(callback_query.from_user.id)['s_of_rf_']]:
            CityKeybord.add(types.InlineKeyboardButton(text=f"{i}",
            callback_data=f"s_c_{i}"))
        CityKeybord.adjust(2)
        await callback_query.bot.send_message(callback_query.from_user.id,'Скажите, в каком городе Вас интересуют вакансии?',reply_markup=CityKeybord.as_markup() )
    
#выбор типа вакансии
@router.callback_query(lambda query: query.data[0:len('s_c_')] == "s_c_")
async def callback_data_handler(callback_query: CallbackQuery):
        ch.ap(callback_query.from_user.id,'s_c_',callback_query.data[len(callback_query.data)-callback_query.data[::-1].index("_"):])
        print(ch.show(callback_query.from_user.id))
        await callback_query.bot.send_message(callback_query.from_user.id,'Выберите тип вакансии',reply_markup=vacancy_typeKeybord.as_markup() )
    
#вывод выбраыннх вакансий  
@router.callback_query(lambda query: query.data[0:len('v_t_')] == "v_t_")
async def callback_data_handler(callback_query: CallbackQuery):
        ch.ap(callback_query.from_user.id,'v_t_',callback_query.data[len(callback_query.data)-callback_query.data[::-1].index("_"):])
        Keybord = InlineKeyboardBuilder()
        vacancy = vacancy_name(ch.show(callback_query.from_user.id)['s_of_rf_'],ch.show(callback_query.from_user.id)['s_c_'],ch.show(callback_query.from_user.id)['v_t_'])
        if len(vacancy) != 0:
            for i in range(len(vacancy)):
                Keybord.add(types.InlineKeyboardButton(text=f"{vacancy[i]}",
                callback_data=f"c_v_{vacany_id(vacancy[i])}"))
            Keybord.add(types.InlineKeyboardButton(
                text="Вернуться в главное меню",
                callback_data="menu"))
            Keybord.adjust(1)
            await callback_query.bot.send_message(callback_query.from_user.id,'Представляю выборку вакансий по Вашему запросу.\nСпасибо, что выбрали ОАО «РЖД» в качестве потенциального работодателя, наша компания это ценит и надеется увидеть Вас в числе наших сотрудников😊',reply_markup=Keybord.as_markup() )        
        else:
            await callback_query.bot.send_message(callback_query.from_user.id,'К сожалению, по Вашему запросу вакансии отсутствуют. Предлагаем рассмотреть вакансии в Вашем регионе\n\nСпасибо, что выбрали ОАО «РЖД» в качестве потенциального работодателя😊',reply_markup=GoBackKeybord.as_markup() )
#выбранная вакансия
@router.callback_query(lambda query: query.data[0:len('c_v_')] == "c_v_")
async def callback_data_handler(callback_query: CallbackQuery):
    name = vacanacy_vacanacy(int(callback_query.data[4:]))
    vancy = vacancy_show(ch.show(callback_query.from_user.id)['s_of_rf_'],ch.show(callback_query.from_user.id)['s_c_'],ch.show(callback_query.from_user.id)['v_t_'],name)
    #много разного не понятного текста тутбудет пока пусто потом доделать
    await callback_query.bot.send_message(callback_query.from_user.id,f'{vacancy_cool(vancy)}',reply_markup=GoBackKeybord.as_markup() )


#see resume
#выбор субъекта
@router.callback_query(lambda query: query.data == "need_worker")
async def callback_data_handler(callback_query: CallbackQuery):
        await callback_query.bot.send_message(callback_query.from_user.id,'Скажите, в каком субъекте РФ Вас интересуют вакансии?',reply_markup=Need_worker_subjectKeybord.as_markup() )

#выбор города 
@router.callback_query(lambda query: query.data[0:len('n_w_s_of_rf_')] == "n_w_s_of_rf_")
async def callback_data_handler(callback_query: CallbackQuery):
        ch_resume.ap(callback_query.from_user.id,'n_w_s_of_rf_',callback_query.data[len(callback_query.data)-callback_query.data[::-1].index("_"):])
        # print(ch_resume.show(callback_query.from_user.id))
        CityKeybord = InlineKeyboardBuilder()
        for i in n_w_city[int(ch_resume.show(callback_query.from_user.id)['n_w_s_of_rf_'])]:
            CityKeybord.add(types.InlineKeyboardButton(text=f"{i}",
            callback_data=f"n_w_s_c_{i}"))
        CityKeybord.adjust(2)
        await callback_query.bot.send_message(callback_query.from_user.id,'Скажите, в каком городе Вас интересуют вакансии?',reply_markup=CityKeybord.as_markup() )

#подтверждение выбора города и субъекта рф 
@router.callback_query(lambda query: query.data[0:len('n_w_s_c_')] == "n_w_s_c_")
async def callback_data_handler(callback_query: CallbackQuery):
        ch_resume.ap(callback_query.from_user.id,'n_w_s_c_',callback_query.data[len(callback_query.data)-callback_query.data[::-1].index("_"):])
        await callback_query.bot.send_message(callback_query.from_user.id,'Подтверждение выбора города и субъекта РФ ',reply_markup=YesNoKeybord.as_markup() )
#вывод выбраыннх резюме
@router.callback_query(lambda query: query.data == "yes")
async def callback_data_handler(callback_query: CallbackQuery):
    resumes = resume_show_2(ch_resume.show(callback_query.from_user.id)['n_w_s_of_rf_'],ch_resume.show(callback_query.from_user.id)['n_w_s_c_'])
    print(ch_resume.show(callback_query.from_user.id)['n_w_s_of_rf_'],ch_resume.show(callback_query.from_user.id)['n_w_s_c_'])
    resumesKeybord = InlineKeyboardBuilder()
    print(resumes.values())
    for i in resumes.values():
        print(i)
        print(i[0])
        resumesKeybord.add(types.InlineKeyboardButton(text=f"{i[0]}",callback_data=f"load_resume_{i[0]}"))
    await callback_query.bot.send_message(callback_query.from_user.id,'Выберите резюме',reply_markup=resumesKeybord.as_markup())


@router.callback_query(lambda query: query.data[0:len('load_resume_')] == "load_resume_")
async def callback_data_handler(callback_query: CallbackQuery,bot : Bot):
    print(callback_query.data[len(callback_query.data)-callback_query.data[::-1].index("_"):])
    document = FSInputFile(f'{callback_query.data[len(callback_query.data)-callback_query.data[::-1].index("_"):]}')
    await bot.send_document(callback_query.from_user.id, document)
    # await callback_query.bot.send_message(callback_query.from_user.id,'Выберите резюме',reply_markup=resumesKeybord.as_markup())


#load resume
@router.callback_query(lambda query: query.data == "load_resume")
async def callback_data_handler(callback_query: CallbackQuery,state: FSMContext):
    await callback_query.bot.send_message(callback_query.from_user.id,'Загрузите файл с резюме docx/pdf форматы')
    await state.set_state(Form.file1)

@router.message(Form.file1)
async def file_test(message: types.Message, state: FSMContext,bot: Bot):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    ch_resume.ap(message.from_user.id,'file_path',file_path)
    if fnmatch.fnmatch(file_path, '*.pdf') or fnmatch.fnmatch(file_path, '*.docx'):
        # await message.answer(f"файл {file_path} загружен")
        await message.answer(f"введите ФИО")
        await state.set_state(Form.file2)
    else:
        await message.answer(f"Файл не соответсвует выбранному формату")

@router.message(Form.file2)
async def file_test(message: types.Message, state: FSMContext,bot: Bot):
    fio=message.text
    ch_resume.ap(message.from_user.id,'fio',fio)
    await message.answer(f"Введите Город")
    await state.set_state(Form.file3)

@router.message(Form.file3)
async def file_test(message: types.Message, state: FSMContext,bot: Bot):
    city=message.text
    ch_resume.ap(message.from_user.id,'city',city)
    await message.answer(f"Введите Субъект федерации")
    await state.set_state(Form.fileload)

@router.message(Form.fileload)
async def file_load(message: types.Message, state: FSMContext,bot: Bot):
    Subject_of_rf=message.text
    ch_resume.ap(message.from_user.id,'Subject_of_rf',Subject_of_rf)
    fio=ch_resume.show(message.from_user.id)['fio']
    city=ch_resume.show(message.from_user.id)['city']
    Subject_of_rf=ch_resume.show(message.from_user.id)['Subject_of_rf']
    file_path = ch_resume.show(message.from_user.id)['file_path']
    if fnmatch.fnmatch(file_path, '*.pdf'):  
        resume_add(message.from_user.id,f"{fio}.pdf",city,Subject_of_rf)
        await bot.download_file(file_path, f"{fio}.pdf")
        await message.answer(f"Файл {fio}.pdf загружен ",reply_markup=GoBackKeybord.as_markup())
    elif fnmatch.fnmatch(file_path, '*.docx'):
        resume_add(message.from_user.id,f"{fio}.pdf",city,Subject_of_rf)
        await bot.download_file(file_path, f"{fio}.docx")
        await message.answer(f"Файл {fio}.docx загружен",reply_markup=GoBackKeybord.as_markup())
