import json
def load_commits(path: str) -> list[dict]:


    """
    Load commits from JSON. Raise FileNotFoundError with a clear
    message if missing, ValueError if the file isn't valid JSON.
    """

    try:

        with open(path) as file:

            return json.load(file)
        
    except FileNotFoundError:

        raise FileNotFoundError("File not foun")
    
    except json.JSONDecodeError:

        raise ValueError("JSON file does not exist")



def commits_per_author(commits: list[dict]) -> dict[str,int]:

    """
    Return {author: commit_count}. Use a comprehension or
    collections.Counter — your choice.
    """

    total_commits = {}

    for commit in commits:

        if commit["author"] in total_commits:

            total_commits["author"] += 1
        else:

            total_commits["author"] = 1
    
    return total_commits




def top_n_largest_commits(commits: list[dict], n: int = 10) -> list[dict]:

    """
    Return the n commits with the highest (lines_added + lines_deleted).
    Sort with a key function — no manual sorting.
    """
     
    return sorted(commits, key = lambda x : x["lines-added"], reverse=True)
