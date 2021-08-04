import click
import re
from typing import List, Dict, Optional
from functools import reduce
from pprint import pprint


def read_file(filepath: str) -> str:
    """
    Opens the given file to read all the contents into a single value, replacing unicode errors with a '?'.
    """
    file = open(filepath, errors="replace")
    content = file.read()
    file.close()
    return content

def get_alpha(string: str) -> str:
    """
    Removes all non-alpha characters from the input
    """
    non_alpha_pattern = r"[^a-zA-Z ]"
    return re.sub(pattern=non_alpha_pattern, repl='', string=string)

def get_word_counts(string: str) -> Dict[str, int]:
    split_words = string.split()
    counts = {}
    for word in split_words:
        old_value = counts.get(word, 0)
        counts[word] = old_value + 1
    return counts

def get_top_words(word_counts: Dict[str, int], top: int = 25) -> Dict[str, int]:
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top]
    return {
        word: count
        for word, count in top_words
    }

def get_stopwords(stopword_path: str) -> List[str]:
    file_content = read_file(stopword_path)
    return file_content.split()

def remove_words(string: str, to_remove: List[str]) -> str:
    removal_join = "|".join(to_remove)
    removal_pattern = f"({removal_join})"
    return re.sub(pattern=removal_pattern, repl='', string=string) 

@click.group()
def cli():
    pass

@click.command()
@click.option("--filepath", help="Filepath to count words from", required=True)
@click.option("--stopword-path", help="Filepath containing list of stopwords")
def word_count(filepath: str, stopword_path: Optional[str]):
    stopwords = []
    if stopword_path:
        stopwords = get_stopwords(stopword_path)
    file_contents = read_file(filepath)
    alpha_content = get_alpha(file_contents)
    no_stopwords = remove_words(alpha_content, stopwords)
    word_counts = get_word_counts(no_stopwords)
    top_words = get_top_words(word_counts)
    click.echo(top_words)

if __name__ == "__main__":
    cli.add_command(word_count)
    cli()
