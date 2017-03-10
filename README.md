# FM Index

A compressed data structure for efficiently searching strings.

## Usage

```python
from fmindex import FMIndex


text = "ababcabcd"
index = FMIndex(text)
occurrences = index.find("ab")
print(occurrences)

```

will print `[0, 2, 5]`


## Installation

    pip install fmindex

## Testing

From the root directory run:

    python -m pytest test

If you don't have `pytest`:

    pip install pytest

## Contributing

Contributors of all levels of experience are welcome!
As of now, the best way to get involved is to comment on an open issue you'd like to pick off.
You could also create an issue to request a feature or report a bug.