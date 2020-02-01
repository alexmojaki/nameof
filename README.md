# nameof

[![Build Status](https://travis-ci.org/alexmojaki/nameof.svg?branch=master)](https://travis-ci.org/alexmojaki/nameof) [![Supports Python versions 3.4+, including PyPy](https://img.shields.io/pypi/pyversions/nameof.svg)](https://pypi.python.org/pypi/nameof)

Get the name of a variable or attribute, as in C#.

## Installation

    pip install nameof

Or just copy `nameof.py`.

## Usage

```python
from nameof import nameof
assert nameof(foo) == "foo"
assert nameof(foo.bar) == "bar"
```

The argument must be a variable or attribute.

## Caveats

This is funky and not battle-tested, use it with caution. If anything critical depends on it working correctly the calling code should be tested.

Doesn't work in the presence of some other magic, particularly magic that modifies the AST such as pytest or [birdseye](https://github.com/alexmojaki/birdseye).
