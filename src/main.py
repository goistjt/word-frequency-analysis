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

def get_word_list(string: str) -> str:
    """
    Removes all non-alpha characters from the input and returns the list of resulting strings
    """
    non_alpha_pattern = r"[^a-zA-Z ]"
    return re.sub(pattern=non_alpha_pattern, repl='', string=string).split()

def get_word_counts(word_list: List[str]) -> Dict[str, int]:
    """
    Builds a map of word->count
    """
    counts = {}
    for word in word_list:
        old_value = counts.get(word, 0)
        counts[word] = old_value + 1
    return counts

def get_top_words(word_counts: Dict[str, int], top: int = 25) -> Dict[str, int]:
    """
    Sorts the word_counts dictionary in descending order by value, and returns top items
    """
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top]
    return {
        word: count
        for word, count in top_words
    }

def get_stopwords(stopword_path: str) -> List[str]:
    """
    Extracts the stopwords from stopword_path and returns them as a list
    """
    file_content = read_file(stopword_path)
    return file_content.split()

def remove_words_from_count(word_count: Dict[str, int], to_remove: List[str]) -> Dict[str, int]:
    """
    Removes all strings in to_remove from the word_count
    """
    copy_count = {**word_count}
    for removal in to_remove:
        copy_count.pop(removal, None)
    return copy_count

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
    word_list = get_word_list(file_contents)
    word_counts = get_word_counts(word_list)
    word_count_without_stops = remove_words_from_count(word_counts, stopwords)
    top_words = get_top_words(word_count_without_stops)
    click.echo(top_words)

if __name__ == "__main__":
    cli.add_command(word_count)
    cli()
