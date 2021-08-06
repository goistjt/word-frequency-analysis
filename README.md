# Word Frequency Analysis

## Frameworks Used
- [click](https://click.palletsprojects.com/en/8.0.x/): Simple CLI Creation Kit with convenient argument parsing and automatic help generation
- [poetry](https://python-poetry.org/): Dependency and virtual environment management

## Setup
0. [Install Python](https://www.python.org/) (At least version 3.8)
1. [Install poetry](https://python-poetry.org/docs/#installation)
2. `poetry install` to download dependencies and configure the virtual environment

## Usage instructions
From the project root, run `poetry run python src/main.py` to view the list of commands. Each command can be run via `poetry run python src/main.py <command> --help` to view the supported and required options.

Any filepaths should be absolute, or relative to the project root (`word-frequency-analysis/`)

## Examples

Run with all supported options used
```zsh
❯ poetry run python src/main.py word-count --filepath res/exercisedocument.txt --stopword-path res/stopwords.txt --word-stems 1 --save 1 --results-path out/results.json
{'YVEAZ': 45,
 'XSDQZ': 32,
 'MFVKEVW': 22,
 'AEO': 16,
 'DSLH': 15,
 'IHNA': 14,
 'MDVQSZ': 14,
 'UEWMK': 13,
 'KHHS': 13,
 'LKFQR': 13,
 'BFLK': 12,
 'NDQZ': 11,
 'F': 11,
 'XZLK': 11,
 'CZHCSZ': 10,
 'VZJ': 10,
 'SDUWZ': 10,
 'HVZ': 9,
 'SDJ': 9,
 'KENZ': 9,
 'IFKKEVW': 9,
 'HFKQHHU': 9,
 'ZPZV': 9,
 'LKZZS': 9,
 'WHPZUVNZVK': 8}
```

Review previous results
```zsh
❯ poetry run python src/main.py review
[{'filepath': 'res/exercisedocument.txt',
  'id': '5fe9a417-218b-4357-98f6-2ab19201819f',
  'results': {'AEO': 16,
              'BFLK': 12,
              'CZHCSZ': 10,
              'DSLH': 15,
              'F': 11,
              'HFKQHHU': 9,
              'HVZ': 9,
              'IFKKEVW': 9,
              'IHNA': 14,
              'KENZ': 9,
              'KHHS': 13,
              'LKFQR': 13,
              'LKZZS': 9,
              'MDVQSZ': 14,
              'MFVKEVW': 22,
              'NDQZ': 11,
              'SDJ': 9,
              'SDUWZ': 10,
              'UEWMK': 13,
              'VZJ': 10,
              'WHPZUVNZVK': 8,
              'XSDQZ': 32,
              'XZLK': 11,
              'YVEAZ': 45,
              'ZPZV': 9},
  'stopword-path': 'res/stopwords.txt',
  'timestamp': '2021-08-05T20:45:17.996661',
  'word-stems': True},
 {'filepath': 'res/exercisedocument.txt',
  'id': 'd9973b1d-819f-41b3-b3ca-0b256d51b083',
  'results': {'AEO': 16,
              'BFLK': 12,
              'CZHCSZ': 10,
              'DSLH': 15,
              'F': 11,
              'HFKQHHU': 9,
              'HVZ': 9,
              'IFKKEVW': 9,
              'IHNA': 14,
              'KENZ': 9,
              'KHHS': 13,
              'LKFQR': 13,
              'LKZZS': 9,
              'MDVQSZ': 14,
              'MFVKEVW': 22,
              'NDQZ': 11,
              'SDJ': 9,
              'SDUWZ': 10,
              'UEWMK': 13,
              'VZJ': 10,
              'WHPZUVNZVK': 8,
              'XSDQZ': 32,
              'XZLK': 11,
              'YVEAZ': 45,
              'ZPZV': 9},
  'stopword-path': 'res/stopwords.txt',
  'timestamp': '2021-08-05T20:14:19.912251',
  'word-stems': True}]
```