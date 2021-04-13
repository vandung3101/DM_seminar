import streamlit as st
import h2o
import pandas as pd

st.title('Should I reset my life?')
st.write('J4f, we DO NOT take any responsibility')
col1, col2, col3, col4 = st.beta_columns(4)
col5, col6, col7 = st.beta_columns(3)
col8, col9, col10 = st.beta_columns(3)

workclass = col1.selectbox('Workclass', ['Self-emp-not-inc',
                                         'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'])
edu = col2.selectbox('Education', ['Bachelors', 'Some-college', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate',
                                   '1st-4th',  '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'Preschool'])
status = col3.selectbox('Marital status', ['Married-civ-spouse',
                                           'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'])
age = col4.slider('Age', 17, 100)
occ = col5.selectbox('Occupation', ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners',
                                    'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])
rela = col6.selectbox('Relationship', [
    'Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
gender = col7.radio('Gender', ['Female', 'Male'])
race = col8.radio('Race', ['White', 'Asian-Pac-Islander',
                           'Amer-Indian-Eskimo', 'Other', 'Black'])
hour = col9.slider('Hours per week', 1, 99)
coun = col10.selectbox('Native country', ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam',
                                          'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad & Tobago', 'Peru', 'Hong', 'Holand-Netherlands'])

if st.button('This is a button, hit it!'):
    pred = pd.DataFrame([[age, workclass, edu, status, occ, rela, race, gender, hour, coun]], columns=['Age', 'Workclass', 'Education', 'Married', 'Occupation',
                                                                                                       'Relationship', 'Race', 'Gender', 'Hour per week', 'Country'])
    st.write(pred)
    result = h2o.mojo_predict_pandas(pred, 'model.zip')
    if result['predict'][0] == '<=50K':
        st.header('Low ' + str(result['<=50K'][0]))
    else:
        st.header('High ' + str(result['>50K'][0]))
    
