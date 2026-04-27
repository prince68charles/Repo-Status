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

    
    total_commits = {}

    for commit in commits:

        if commit["author"] in total_commits:

            total_commits["author"] += 1
        else:

            total_commits["author"] = 1
    
    return total_commits
