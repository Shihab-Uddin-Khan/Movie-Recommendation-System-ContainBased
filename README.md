#🎬 Movie-Recommendation-System-ContainBased


A **smart and interactive movie recommendation system** built using Scikit-learn, Streamlit, and TMDB API**. This project allows users to explore movies and get personalized recommendations with posters, ratings, and more, all through a sleek web interface.

---

## 🔗 Live Demo

Check out the live application [here](https://huggingface.co/spaces/qShihab/Movie-Recommendation-System)  
> The app is deployed on **Hugging Face Spaces**, providing a seamless user experience without installation.

## Must requirement (must read)
- Due to very large size I was unable to upload the datasets and the `similarity.joblib` file.  
- You can download those files from the Google Drive link below.
  Download the files from [here](https://huggingface.co/spaces/qShihab/Movie-Recommendation-System](https://drive.google.com/file/d/1oGEX1hWysly4Ww2QujIS4adhvGebfKy8/view?usp=sharing)  
- To run this code on Streamlit use:  
  ```bash
  python -m streamlit run app.py

## 📸 Screenshots
**Home Page**  
![Home Screenshot]
<img width="1914" height="895" alt="Screenshot 2025-08-30 220639" src="https://github.com/user-attachments/assets/872e870c-86ca-4b60-8f1b-dc07589eecd9" />

**Recommendation Page**  
![Recommendation Screenshot]

<img width="1885" height="898" alt="Screenshot 2025-08-30 220701" src="https://github.com/user-attachments/assets/b7f1826e-701c-4db1-96bb-fa75313c19f4" />
<img width="1902" height="884" alt="Screenshot 2025-08-30 220719" src="https://github.com/user-attachments/assets/8a163368-a7bd-4ec3-a347-4fb7db0336fc" />



## 🛠 Features

- **Movie Recommendations**: Get movie suggestions based on your favorite titles.  
- **Poster Display**: Shows the poster image fetched from TMDB API.  
- **Interactive Search**: Search movies by name and instantly get recommendations.  
- **Data Handling**: Uses **Pickle and Pandas** for efficient data processing.  
- **Easy Deployment**: Fully deployed online, no local setup required.  

---

## 📝 Technologies Used

This project leverages modern Python libraries and frameworks to deliver a fast, interactive, and visually appealing movie recommendation system.  

- **Python 3.x** – Core programming language for backend logic and data processing.  
- **Streamlit** – Web framework for building an interactive, user-friendly app interface.  
- **Pandas** – Data manipulation and preprocessing, including cleaning and organizing movie datasets.  
- **Pickle** – Efficient storage and retrieval of preprocessed datasets, such as similarity matrices.  
- **Requests** – Handles API calls to **TMDB** to fetch movie posters and additional metadata dynamically.  
- **Scikit-learn** – Provides tools to compute similarity metrics (e.g., cosine similarity) for the recommendation engine.  


