import pandas as pd
import fnmatch


df= pd.read_excel("resume.xlsx","Лист1")
df2= pd.read_excel("resume1.xlsx","Лист1")
def resume_add(id,path,city,Subject_of_rf,df=df,df2=df2):

    if fnmatch.fnmatch(path, '*.pdf'):
        path = f'{path}.pdf'
    elif fnmatch.fnmatch(path, '*.docx'):
        path = f'{path}.docx'
    df.loc[len(df.index)] = [id,path,city,Subject_of_rf]
    df2.loc[len(df2.index)] = [df2.iloc[-1, df2.columns.get_loc('id')] + 1,Subject_of_rf]
    df.to_excel("resume.xlsx","Лист1",index=False)
    df2.to_excel("resume1.xlsx","Лист1",index=False)

# resume_add(3525,"pat","xcvdfg","sdfsdf")

def resume_sub_id(name,df=df2):
    return df[df['Субъект федерации'] == name]['id'].to_list()[0]

def resume_sub_name(id,df=df2):
    return df[df['id'] == id]['Субъект федерации'].to_list()[0]

def vacancies_by_city(df=df):
    subject={resume_sub_id(i):set() for i in df['Субъект федерации'].unique()}
    for i in df['Субъект федерации'].unique():
        i1=resume_sub_id(i)
        for j in df[df['Субъект федерации']==i]['Город'].unique():
            subject[i1].add(j)
    return subject
n_w_city=vacancies_by_city()
def resume_show(id,df=df):
    return df[df['id'] == id]['resume_path'].to_list()

def resume_vacancies_by_city(df=df):
    subject={i:set() for i in df['Субъект федерации'].unique()}
    for i in df['Субъект федерации'].unique():
        for j in df[df['Субъект федерации']==i]['Город'].unique():
            subject[i].add(j)
    return subject

def resume_show_2(obj,city,df=df):
    obj=int(obj)
    obj = resume_sub_name(obj)
    return df[(df['Субъект федерации']==obj) & (df['Город']==city)][['path']].to_dict()


# print(resume_show_2('1','Москва'))
# print(resume_show('Центральный','Москва'))
# res = resume_show('Центральный','Москва').to_dict()
# print(res)
# for i in res.values():
#     print()
# print(n_w_city)
# print(resume_sub_id(1))