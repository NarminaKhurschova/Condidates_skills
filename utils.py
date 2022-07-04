import json

def load_candidates_list():
    with open ("candidates.json") as file:
        candidates_list = json.load(file)
        return candidates_list