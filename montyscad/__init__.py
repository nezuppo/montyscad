#!/usr/bin/env python3

import numpy as np
from decimal import Decimal

class Scad(list):
    def write(self, filename):
        with open(filename, 'w') as f:
            for one in self:
                f.write(str(one) + '\n')

class Symbol(list):
    _one_indent = '  '

    def __init__(self, name, *args, **kwargs):
        super().__init__()

        self._name = name
        self.args = args
        self.kwargs = kwargs
        self.indent = 0
        self.modifier = None

    def __val2str(self, val):
        assert not isinstance(val, float), ('use Decimal instead of float', val)

        if isinstance(val, bool):
            # bool must be processed before int
            return 'true' if val else 'false'
        if isinstance(val, int):
            return str(val)
        if isinstance(val, np.int64):
            return str(val)
        if isinstance(val, Decimal):
            return str(val)
        if isinstance(val, str):
            return '"{}"'.format(val)
        if isinstance(val, list) or isinstance(val, np.ndarray):
            return '[{}]'.format(', '.join([self.__val2str(one) for one in val]))

        raise Exception(type(val), val)

    def _str_1st_line(self):
        arg_strs = []

        arg_strs += [
            self.__val2str(arg)
            for arg in self.args
        ]

        arg_strs += [
            '{}={}'.format(name, self.__val2str(val))
            for name, val in self.kwargs.items()
        ]

        return '{}{}{}({})'.format(
            self._one_indent * self.indent,
            self.modifier if self.modifier is not None else '',
            self._name,
            ', '.join(arg_strs)
        )

    def __str__(self):
        string = self._str_1st_line()

        if len(self) == 0:
            string += ';'
        else:
            string += ' {\n'
            for child in self:
                child.indent = self.indent + 1
                string += '{}\n'.format(child)
            string += '{}}}'.format(self._one_indent * self.indent)
        return string

    def modify(self, modifier='#'):
        self.modifier = modifier
        return self

    def add_others(self, *args):
        for other in args:
            self.append(other)

        return self

class Module(Symbol):
    def __init__(self, name=None):
        if not name:
            name = self.__class__.__name__

        super().__init__(name)

    def _str_1st_line(self):
        return '{}module {}()'.format(
            self._one_indent * self.indent,
            self._name
        )
