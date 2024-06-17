import streamlit as st

st.title('hey i am getting started')
st.header('header -> hey i am getting started')
st.subheader('subheaderhey -> i am getting started')
st.text('text -> hello this is text')

st.markdown('# this is markdown')
st.markdown('# hello')
st.markdown('## hello')
st.markdown('### hello')
st.markdown('#### hello')

st.success('sucess')  #sucess
st.info('information!') #information
st.warning('warning!') #warning
st.error('error!') #error


exp = ZeroDivisionError('division is not possible with zero')
st.exception(exp)


st.help(ZeroDivisionError) #help

#write function
st.write("range(1-10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

#code
st.code('x=10 \n'
        'for i in range(x): \n'
         '    print(i)')


#checkbox
st.checkbox('Male')
st.checkbox('Female')  #two same checkbox names cant be written

if(st.checkbox('Adult')):
    st.write('you are an adult get serious in life!!')



#radio - no multiple selections
#st.radio('select gender : ',('male','female','you better die!'))

radioButton = st.radio('select gender : ',('male','female','other'))

if(radioButton == 'male'):
    st.write("you'r vengence")
elif(radioButton == 'female'):
    st.write('congrats your a female')
elif(radioButton == 'other'):
    st.write("You better die!")

#selectbox -selection box
st.subheader('select box')
selectBox = st.selectbox("Data Science Domains : ",['select from here','data analasis','web scrappig','machine learning',
                                        'deep learning','NLP','Image Processing'])
st.write('you have selected: ',selectBox)

#multiselect box
st.subheader('multiselect box')
multiSelectbox = st.multiselect("Data Science Domains : ",['data analasis','web scrappig','machine learning',
                                        'deep learning','NLP','Image Processing'])

st.write("you have selected: ",len(multiSelectbox),multiSelectbox)
st.write("you have selected: ",len(multiSelectbox),'courses')


#button
st.write("button")
#st.button('click me')
if(st.button('touch me')):
    st.write('thanks for clicking me')
    

#slider
st.subheader('slider')
lvl = st.slider('select the level',1,100,step=1)
st.write('level is : ',lvl)


#input command
st.subheader('text input')
name = st.text_input('your Name: ')
if(name):
    st.write('hello',name)

st.header('input a user and password')
user = st.text_input('username : ')
password = st.text_input('password : ',type='password')

#text area
st.header('Text Area')
textArea = st.text_input('write something intrsting about yourself',)
st.write(textArea)

#input number,date,time
st.subheader('input number')
st.number_input('select your age',18,85)

st.subheader('input date')
st.date_input('date')

st.subheader('input time')
st.time_input('time')

#display the pic's

