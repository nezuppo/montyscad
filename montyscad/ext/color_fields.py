#!/usr/bin/env python3

from montyscad import monty_symbols as ms
from montyscad import (
    Symbol,
)

class Colors:
    __colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    ]
    __next_color_index = 0
    
    @classmethod
    def get_next_color(cls):
        next_color = cls.__colors[cls.__next_color_index]
        cls.__next_color_index = (cls.__next_color_index + 1) % len(cls.__colors)

        return next_color

class ColorFields(list):
    ALL   = 0
    UNION = 1
    PLAIN = 2

    def __init__(self, pluses, minuses=None, pluses2=None):
        super().__init__()

        self._pluses  = self.__normalize_symbols(pluses)
        self._minuses = self.__normalize_symbols(minuses)
        self._pluses2 = self.__normalize_symbols(pluses2)

    def __normalize_symbols(self, symbols):
        if isinstance(symbols, Symbol):
            return [symbols]
        elif isinstance(symbols, list):
            return symbols
        elif symbols is None:
            return []
        else:
            raise Exception(type(symbols))

    def __iadd__(self, other):
        assert isinstance(other, ColorFields), type(other)

        self._pluses  += other._pluses
        self._minuses += other._minuses
        self._pluses2 += other._pluses2

        return self

    def __get_diff(self, height, target, follows):
        symbol = ms.difference()
        symbol.append(target)
        symbol += follows

        if height is not None:
            symbol = ms.linear_extrude(height).add_others(symbol)
        symbol = ms.color(Colors.get_next_color()).add_others(symbol)

        return symbol

    def __get_symbol_colored(self, height, cf_mode):
        union = ms.union()

        for i in range(len(self._pluses)):
            symbol = self.__get_diff(height, self._pluses[i],
                    self._pluses[i + 1:] + self._minuses + self._pluses2)
            union.append(symbol)

        if cf_mode == self.ALL:
            for i in range(len(self._minuses)):
                symbol = self.__get_diff(height, self._minuses[i],
                        self._minuses[i + 1:] + self._pluses2)
                union.append(symbol)

        for i in range(len(self._pluses2)):
            symbol = self.__get_diff(height, self._pluses2[i],
                    self._pluses2[i + 1:])
            union.append(symbol)

        return union

    def __get_symbol_plain(self, height):
        assert self._pluses
        symbol = ms.union()(*self._pluses) if 1 < len(self._pluses) else self._pluses[0]

        if self._minuses:
            symbol = ms.difference()(
                symbol,
                *self._minuses
            )

        if self._pluses2:
            symbol = ms.union()(
                symbol,
                *self._pluses2
            )

        symbol = ms.linear_extrude(height)(symbol)

        return symbol

    def _insert_in_list(self, target_list, symbol, index):
        if index is None:
            if isinstance(symbol, Symbol):
                target_list.append(symbol)
            elif isinstance(symbol, list) or isinstance(symbol, tuple):
                target_list += symbol
            else:
                raise Exception(type(symbol))
        else:
#
            raise Exception('write here')

    def insert_in_pluses(self, symbol, index=None):
        self._insert_in_list(self._pluses, symbol, index)

    def insert_in_minuses(self, symbol, index=None):
        self._insert_in_list(self._minuses, symbol, index)

    def insert_in_pluses2(self, symbol, index=None):
        self._insert_in_list(self._pluses2, symbol, index)

    def get_symbol(self, height=None, cf_mode=ALL):
        if cf_mode in (self.ALL, self.UNION):
            return self.__get_symbol_colored(height, cf_mode)
        if cf_mode == self.PLAIN:
            return self.__get_symbol_plain(height)
        raise Exception(cf_mode)

    def _translate_symbols(self, translate_v, symbols):
        for i, one in enumerate(symbols):
            symbols[i] = ms.translate(translate_v)(one)

    def translate(self, translate_v):
        self._translate_symbols(translate_v, self._pluses)
        self._translate_symbols(translate_v, self._minuses)
        self._translate_symbols(translate_v, self._pluses2)
