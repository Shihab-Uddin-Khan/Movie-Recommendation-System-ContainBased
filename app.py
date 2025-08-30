# ---------------------Importing libraies--------------------------------------
import streamlit as st
import pickle
import pandas as pd
import requests

# ----------Fetch_poster of the movie with the help movie_id and with the help of tmdb api servies------------.
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ddde7f58944bf0bfc384663dd435a0b7'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']


# -------Recommends movies on the based on similartiy array------------.
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movies_id = movies.iloc[i[0]].movie_id
        # fatch post form api
        recommended_movies_posters.append(fetch_poster(movies_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies , recommended_movies_posters


# ----------Reading the movies.pkl----------------------- ,
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
import joblib
# load similarity with joblib instead of pickle
similarity = joblib.load('similarity.joblib')


# ----------------- Background + Styling -----------------
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --------------------Call it at the top-----------------------
add_bg_from_local("background.jpg")

# --------------Creating a selectbox of the movies--------------
st.title('Movie Recommender system')
selected_movie_name = st.selectbox(
    'Which movie would you like to recommended?',
    movies['title'].values
)
# ---------------button fo the recommendations------------------
if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie_name)
# ----------------Showing the recommended movies----------------
    # First row (5 columns)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    # Second row (5 columns)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
