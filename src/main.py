import click
import re
from typing import List, Dict
from functools import reduce

from click.core import V

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

@click.group()
def cli():
    pass

@click.command()
@click.option("--filepath", help="Filepath to count words from", required=True)
def word_count(filepath: str):
    file_contents = read_file(filepath)
    alpha_content = get_alpha(file_contents)
    word_counts = get_word_counts(alpha_content)
    top_words = get_top_words(word_counts)
    click.echo(top_words)

if __name__ == "__main__":
    cli.add_command(word_count)
    cli()
