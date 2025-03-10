import streamlit as st
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')
x = ['Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
y = ['Survived']
train_x = train[x]
train_y = train[y]
st.write('общая таблица c данными')
st.dataframe(train)
a1 = st.select_slider('Вывести данные по конкретному пассажиру',options=train['PassengerId'])
st.dataframe(train[train['PassengerId']==a1])
surv = ['Survived','not survived']
st.write('выберите один из признаков по которому будем делать сравнение')
x1 = st.pills('attribute',options=x,selection_mode='single',default=x[0])
#y1 = st.pills('show passengers: survived and/or not survived',options=surv,selection_mode='multi',default=surv[0])

st.write(*[x1,f'/ {y[0]}'])
st.scatter_chart(train, y=y[0], x=x1)
st.plotly_chart(px.histogram(train,x=x1,y=y[0]))





