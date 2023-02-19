#!/usr/bin/env python
# coding: utf-8

# In[74]:


import numpy as np
from scipy.stats import t
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Задание 1. Загрузите файл HR.csv в pandas dataframe.

# In[75]:


data=pd.read_csv(r'\Users\super\Desktop\HR.csv')
data.head()


# Задание 2. Рассчитать основные статистики для переменных (среднее,медиана,мода,мин/макс,сред.отклонение).
# 

# In[76]:


data.dtypes


# In[77]:


data.describe()


# In[78]:


data.mode()


# Задание 3.Рассчитать и визуализировать корреляционную матрицу для переменных.

# In[79]:


sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.2)
fig=plt.gcf()
fig.set_size_inches(12,12)
plt.show()


# Вывод: Здесь мы видим, что переменные (average_monthly_hours - Среднее количество часов на рабочем месте в месяц) и (Last_evaluation - Время с момента последней оценки в годах) имеют зависимость от переменной (number_projects - Количество проектов, выполненных за время работы). Также у них заметна положительная корреляция. Переменная "Уровень удовлетворенности" и переменная "Сотрудники, которые сейчас работают" имеет отрицательную корреляцию.

# Здание 4. Рассчитайте сколько сотрудников работает в каждомдепартаменте.

# In[80]:


def groupby_function(data):
    return data.satisfaction_level.count()


# In[81]:


print('В департаментах работает : \n', data.groupby('department').apply(groupby_function))


# Задание 5. Показать распределение сотрудников по зарплатам.

# In[82]:


def groupby_count(data):
    return data.satisfaction_level.count()
df=data.groupby('salary').apply(groupby_count)
df


# In[83]:


r=['low', 'medium' ,'high']
plt.bar(r, df, color = 'white')
plt.rcParams['axes.facecolor'] = 'black'
plt.xlabel('Уровень зарплаты')
plt.ylabel('Количество сотрудников')
plt.title('Плотность распределения значений')
plt.show()


# Задание 6. Показать распределение сотрудников по зарплатам в каждом
# департаменте по отдельности.

# In[84]:


Income_data=data.groupby(['department','salary']).apply(groupby_count).reset_index()
Income_data.columns=['department', 'salary', 'count']
Income_data


# In[85]:


row=Income_data['salary']
f = Income_data['count']
sns.catplot(x='salary', y='count', hue='department', kind='bar', data=Income_data)


# Здание 7. Проверить гипотезу, что сотрудники с высоким окладом
# проводят на работе больше времени, чем сотрудники с низким
# окладом.

# In[86]:


df_high = list(data.loc[data['salary'] == 'high']['average_montly_hours'])
df_low = list(data.loc[data['salary'] == 'low']['average_montly_hours'])


# In[87]:


plt.hist(df_high, bins=100, density=True, color = 'red');
plt.hist(df_low, bins=100, density=True);


# В целом большой разницы в эффективности работы не замечено.

# Задание 8. Рассчитать следующие показатели среди уволившихся и не
# уволившихся сотрудников (по отдельности):
# 
# ● Доля сотрудников с повышением за последние 5 лет
# 
# ● Средняя степень удовлетворенности
# 
# ● Среднее количество проектов

# In[88]:


data_left = data.loc[data['left'] == 1]
data_left.head()


# In[89]:


len(data_left.loc[data_left['promotion_last_5years'] == 1])/len(data_left)


# In[90]:


data_left['satisfaction_level'].mean()


# In[91]:


data_left['number_project'].mean()


# In[92]:


data_noleft = data.loc[data['left'] == 0]
data_noleft.head()


# In[93]:


len(data_noleft.loc[data_noleft['promotion_last_5years'] == 1])/len(data_noleft)


# In[94]:


data_noleft['satisfaction_level'].mean()


# In[95]:


data_noleft['number_project'].mean()


# In[ ]:




