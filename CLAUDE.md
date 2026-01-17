# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

cakeipsum-python is a Python package that generates cake/dessert-themed Lorem Ipsum text. It includes both a CLI tool and a Python API.

## Development Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in editable mode
pip install -e .

# Verify installation
cakeipsum --help
```

## Build Commands

```bash
# Install in editable mode (for development)
pip install -e .

# Build distribution packages
python -m build

# Install from git URL
pip install git+https://github.com/austinogilvie/cakeipsum-python.git
```

## Project Structure

```
src/cakeipsum/
├── __init__.py      # Public API exports
├── words.py         # Dessert word list (59 words)
├── generator.py     # CakeIpsum class with words(), sentences(), paragraphs()
└── cli.py           # CLI using argparse
```

## CLI Usage

```bash
cakeipsum                          # 1 medium paragraph
cakeipsum -p 3                     # 3 paragraphs
cakeipsum -w 20                    # 20 words
cakeipsum -s 5                     # 5 sentences
cakeipsum --long --love            # Long paragraph with "I love" phrases
cakeipsum --start-with-cake-ipsum  # Start with "Cake ipsum dolor sit amet"
```

## Wrangler Integration

This project uses Wrangler for project governance. Issue tracking, specifications, and plans are managed in `.wrangler/`.
