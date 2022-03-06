#!/usr/bin/env python3

from montyscad import Symbol as _Symbol

_symbol_names = [
    'circle',
    'color',
    'cube',
    'cylinder',
    'difference',
    'intersection',
    'linear_extrude',
    'import',
    'minkowski',
    'mirror',
    'offset',
    'projection',
    'rotate',
    'rotate_extrude',
    'sphere',
    'square',
    'translate',
    'union',
]

class _SymbolsBase(_Symbol):
    def __init__(self, *args, **kwargs):
        super().__init__(self.__class__.__name__, *args, **kwargs)

_symbol_names = set(_symbol_names)

_global_symbols = globals()
for _symbol_name in _symbol_names:
    assert _symbol_name not in _global_symbols, (_symbol_name, _global_symbols)
    _symbol_class = type(_symbol_name, (_SymbolsBase,), {})
    _global_symbols[_symbol_name] = _symbol_class
