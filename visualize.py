import os
from collections import Counter
from datetime import datetime


import matplotlib.pyplot as plt
import seaborn as sn

os.makedirs("output", exist_ok=True)

sn.set_theme(style="whitegrid")


def plot_comits_by_author(commits: list[dict]) -> None:


    """Function that plots the number of comits performed by each author"""


    counts = Counter(commit["author"] for commit in commits)
    sorted_items = sorted(counts.items(), key = lambda x: x[1], reverse=True)

    authors = [item[0] for item in sorted_items]
    values = [item[1] for item in sorted_items]


    #Construct the graph

    fig, ax = plt.subplot(figsize=(8,5))
    sn.barplot(x=authors, y =values, ax=ax)

    ax.set_title("Commits per author")
    ax.set_xlabel("Author")
    ax.set_ylabel("Number of commits")

    fig.savefig("output/commits_by_author.png", dpi=120)
    plt.close(fig)