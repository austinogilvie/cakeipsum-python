# cakeipsum

A cake/dessert-themed Lorem Ipsum text generator for Python.

Inspired by [Cupcake Ipsum](https://cupcakeipsum.com/).

## Installation

```bash
pip install git+https://github.com/austinogilvie/cakeipsum-python.git
```

Or install in editable mode for development:

```bash
git clone https://github.com/austinogilvie/cakeipsum-python.git
cd cakeipsum-python
pip install -e .
```

## CLI Usage

```bash
# Generate 1 medium paragraph (default)
cakeipsum

# Generate 3 paragraphs
cakeipsum -p 3

# Generate 20 words
cakeipsum -w 20

# Generate 5 sentences
cakeipsum -s 5

# Generate 2 long paragraphs
cakeipsum -p 2 --long

# Start with "Cake ipsum dolor sit amet"
cakeipsum --start-with-cake-ipsum

# Include "I love" phrases (10% chance)
cakeipsum --love

# Disable line wrapping
cakeipsum --cols 0

# Show help
cakeipsum --help
```

### Options

| Option | Description |
|--------|-------------|
| `-w N, --words N` | Output N words |
| `-s S, --sentences S` | Output S sentences |
| `-p P, --paragraphs P` | Output P paragraphs (default: 1) |
| `--short` | Short paragraphs (3-5 sentences) |
| `--medium` | Medium paragraphs (6-11 sentences, default) |
| `--long` | Long paragraphs (12-15 sentences) |
| `--love` | Include "I love" phrases |
| `--start-with-cake-ipsum` | Start with "Cake ipsum dolor sit amet" |
| `--cols COLS` | Line width for wrapping (default: 80, 0 for no wrap) |
| `-v, --version` | Show version |
| `-h, --help` | Show help |

## Python API

```python
from cakeipsum import CakeIpsum

# Create a generator
gen = CakeIpsum()

# Generate 10 words
print(gen.words(10))

# Generate 3 sentences
print(gen.sentences(3))

# Generate 2 medium paragraphs
print(gen.paragraphs(2, length="medium"))

# With options
gen = CakeIpsum(start_with_cake_ipsum=True, love=True)
print(gen.paragraphs(1))
```

## License

MIT
