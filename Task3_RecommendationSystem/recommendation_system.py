import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie Dataset
movies = {
    "Movie": [
        "Avengers",
        "Iron Man",
        "Captain America",
        "Batman",
        "Superman",
        "Spider-Man",
        "Doctor Strange",
        "Thor"
    ],

    "Genre": [
        "Action Superhero",
        "Action Superhero",
        "Action Superhero",
        "Action DC",
        "Action DC",
        "Action Superhero",
        "Fantasy Superhero",
        "Fantasy Action"
    ]
}

# Create DataFrame
df = pd.DataFrame(movies)

print("Movie Dataset:\n")
print(df)

# Convert genres into numerical vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Genre"])

# Calculate similarity
similarity = cosine_similarity(tfidf_matrix)

# Recommendation Function
def recommend(movie_name):

    # Check whether movie exists
    if movie_name not in df["Movie"].values:
        print("\nMovie not found!")
        print("\nAvailable Movies:")
        for movie in df["Movie"]:
            print("-", movie)
        return

    index = df[df["Movie"] == movie_name].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    for movie in scores[1:4]:
        print(df.iloc[movie[0]]["Movie"])


# User Input
movie = input("\nEnter a movie name: ").strip()

recommend(movie)