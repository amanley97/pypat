# pypat

**pypat** is a Python wrapper for [McPAT](https://www.hpl.hp.com/research/cacti/mcpat/).

## Features

- Reads gem5 `.h5` stats and `.json` configs
- Substitutes `config.*` and `stats.*` values into an XML template
- Runs the McPAT binary on the generated XML

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
cd src 
make
```

## Usage
```bash
python pypat <stats.h5> <config.json>
```