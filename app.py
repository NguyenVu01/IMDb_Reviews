import streamlit as st
import pickle
import sklearn

# load model
model = pickle.load(open('model.pkl', 'rb'))

# create title
st.title('Mô hình phân tích cảm xúc IMDB Reviews')

review = st.text_input('Nhập vào review:')

submit = st.button('Dự đoán')


if submit:
    prediction = model.predict([review])

    if prediction[0] == 'positive':
        st.success('Review Tích cực')
    else:
        st.warning('Review Tiêu cực')

