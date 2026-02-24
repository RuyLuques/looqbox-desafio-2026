import pandas as pd
import matplotlib.pyplot as plt
from src.data_access import movies_imdb

if __name__ == "__main__":
    df = movies_imdb()
    df = df.dropna(subset=["Genre", "Rating"])
    df["Genre"] = df["Genre"].str.split(",")
    df = df.explode("Genre")

    top_genres = df.groupby("Genre")["Rating"].mean().reset_index().sort_values("Rating", ascending=False)
    print(top_genres.head())

    plt.bar(top_genres["Genre"], top_genres["Rating"])
    plt.xticks(rotation=90)
    plt.ylabel("Média Rating")
    plt.title("Média Rating por Gênero")
    plt.tight_layout()
    plt.show()