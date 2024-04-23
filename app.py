import streamlit as st
import pandas as pd
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = [[0]]

        
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendations System')

selected_movie_name = st.selectbox(
    'Movie recommendation based on selection of a movie',
    movies['title'].values
)

if st.button('Recommend Me'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)