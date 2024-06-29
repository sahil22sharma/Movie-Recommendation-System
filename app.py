import pickle
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import requests 

rating = [1,2,3,4,5]
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d08164a07d179c1692fdf3d743b939e9&language=en-US'.format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:26]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values)
ratings = st.selectbox(
    "Enter Ratings",
    rating,
    placeholder="Enter the ratings of the movie",
    index=None
)

if st.button('Show Recommendation'):
    if ratings == 5:
        name,poster = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5,gap='medium')
        with col1:
            st.text(name[0])
            st.image(poster[0])
        with col2:
            st.text(name[1])
            st.image(poster[1])
        with col3:
            st.text(name[2])
            st.image(poster[2])
        with col4:
            st.text(name[3])
            st.image(poster[3])
        with col5:
            st.text(name[4])
            st.image(poster[4])
    elif ratings == 4:
        name,poster = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5,gap='medium')
        with col1:
            st.text(name[5])
            st.image(poster[5])
        with col2:
            st.text(name[6])
            st.image(poster[6])
        with col3:
            st.text(name[7])
            st.image(poster[7])
        with col4:
            st.text(name[8])
            st.image(poster[8])
        with col5:
            st.text(name[9])
            st.image(poster[9])
    elif ratings == 3:
        name,poster = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5,gap='medium')
        with col1:
            st.text(name[10])
            st.image(poster[10])
        with col2:
            st.text(name[11])
            st.image(poster[11])
        with col3:
            st.text(name[12])
            st.image(poster[12])
        with col4:
            st.text(name[13])
            st.image(poster[13])
        with col5:
            st.text(name[14])
            st.image(poster[14])
    elif ratings == 2:
        name,poster = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5,gap='medium')
        with col1:
            st.text(name[15])
            st.image(poster[15])
        with col2:
            st.text(name[16])
            st.image(poster[16])
        with col3:
            st.text(name[17])
            st.image(poster[17])
        with col4:
            st.text(name[18])
            st.image(poster[18])
        with col5:
            st.text(name[19])
            st.image(poster[19])
    elif ratings == 1:
        name,poster = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5,gap='medium')
        with col1:
            st.text(name[20])
            st.image(poster[20])
        with col2:
            st.text(name[21])
            st.image(poster[21])
        with col3:
            st.text(name[22])
            st.image(poster[22])
        with col4:
            st.text(name[23])
            st.image(poster[23])
        with col5:
            st.text(name[24])
            st.image(poster[24])
   
