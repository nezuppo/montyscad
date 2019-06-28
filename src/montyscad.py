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

    def __init__(self, name, **kwargs):
        super().__init__()

        self._name = name
        self.kwargs = kwargs
        self.indent = 0

    def __trans_val(self, val):
        if isinstance(val, int):
            return val
        if isinstance(val, Decimal):
            return float(val)

        raise Exception(val)

    def __get_arg_strs(self):
        arg_strs = []

        for arg_name, arg_val in self.kwargs.items():
            if False:
                pass
            elif isinstance(arg_val, float):
                raise Exception(('forbidden', arg_name, arg_val))
            elif isinstance(arg_val, bool):
                arg_val_str = 'true' if arg_val else 'false'
            elif isinstance(arg_val, list) or isinstance(arg_val, np.ndarray):
                arg_val_str = str([self.__trans_val(one) for one in arg_val])
            elif isinstance(arg_val, Decimal) or isinstance(arg_val, int):
                arg_val_str = str(arg_val)
            elif isinstance(arg_val, str):
                arg_val_str = '"{}"'.format(arg_val)
            else:
                raise Exception(type(arg_val))

            arg_strs.append('{}={}'.format(arg_name, arg_val_str))

        return arg_strs

    def _str_1st_line(self):
        return '{}{}({})'.format(
            self._one_indent * self.indent,
            self._name,
            ', '.join(self.__get_arg_strs())
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

    def add_others(self, *args):
        for other in args:
            self.append(other)

        return self

class Module(Symbol):
    def __init__(self, name):
        super().__init__(name)

    def _str_1st_line(self):
        return '{}module {}()'.format(
            self._one_indent * self.indent,
            self._name
        )
