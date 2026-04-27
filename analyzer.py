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



