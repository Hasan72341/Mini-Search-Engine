# read wikipedia articles from processed folder

import json
from pathlib import Path
import pickle

def read_documents(processed_path):
    # yield title, url, text

    processed_path = Path(processed_path)

    for folder in sorted(processed_path.iterdir()):
        if not folder.is_dir():
            continue

        for wiki_file in sorted(folder.iterdir()):
            if not wiki_file.name.startswith("wiki_"):
                continue

            with wiki_file.open("r", encoding="utf-8") as f:
                for line in f:
                    article = json.loads(line)
                    yield (
                        article.get("title", ""),
                        article.get("url", ""),
                        article.get("text", "")
                    )


# save and load index data

def save_pickle(obj, path):
    path = Path(path)
    with path.open("wb") as f:
        pickle.dump(obj, f)


def save_json(obj, path):
    path = Path(path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f)

# load saved index data


def load_pickle(path):
    with Path(path).open("rb") as f:
        return pickle.load(f)


def load_json(path):
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)
