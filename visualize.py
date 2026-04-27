import os
from collections import Counter
from datetime import datetime


import matplotlib.pyplot as plt
import seaborn as sn

os.makedirs("output", exist_ok=True)

sn.set_theme(style="whitegrid")


def plot_comits_by_author(commits: list[dict]) -> None:


    """Function that plots the number of comits performed by each author"""


    counts = Counter(c["author"] for c in commits)
    sorted_items = sorted(counts.items(), key = lambda x: x[1], reverse=True)

    authors = [item[0] for item in sorted_items]
    values = [item[1] for item in sorted_items]


    #Construct the graph

    fig, ax = plt.subplots(figsize=(8,5))
    sn.barplot(x=authors, y =values, ax=ax)

    ax.set_title("Commits per author")
    ax.set_xlabel("Author")
    ax.set_ylabel("Number of commits")

    fig.savefig("output/commits_by_author.png", dpi=120)
    plt.close(fig)


def commits_over_time(commits: dict[str, int]) -> None:


    """Function that plots commits over time via a bargraph"""

    dates = (datetime.fromisoformat(commit["timestamp"].date() for commit in commits))
    counts = Counter(dates)

    sorted_dates = sorted(counts.keys())
    values = [counts[d] for d in sorted_dates]


    #Create Line Chart

    fig, ax = plt.subplots(figsize = (10,5))

    ax.plot(sorted_dates, values, marker = "o", linewidth = 1.5)

    ax.set_title("Commits over time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Commits")

    # Rotate the x-axis labels 45 degrees so they don't overlap
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    fig.tight_layout()
    fig.savefig("output/commits_over_time.png", dpi=120)
    plt.close(fig)