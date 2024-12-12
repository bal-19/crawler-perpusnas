# Perpusnas Crawler Crawler

get all data from https://data.perpusnas.go.id

## Usage/Examples

```bash
python source/main.py --output=data_perpustakaan --destination=mongo crawler --mode=perpusnas --type=get_perpustakaan
```

## Requirements

**Python Version:** [3.10.14](https://www.python.org/downloads/release/python-31014/)

## Installation

clone project using git

```bash
git clone https://github.com/bal-19/crawler-perpusnas.git
```

go to directory

```bash
cd crawler-perpusnas
```

create python virtual environment

```bash
python -m venv .venv
```

activate virtual environment

-   Windows

```bash
.venv/Scripts/Activate.ps1
```

-   Linux

```bash
source .venv/bin/activate
```

install project requirements

```bash
pip install -r source/requirements.txt
```

start project

```bash
python3 source/main.py --help
```
