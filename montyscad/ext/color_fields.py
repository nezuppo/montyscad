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
#
        """ <
        all_sets = self.union_color_sets + self.minus_color_sets
        len_colors = len(self.colors)

        len_all = len(all_sets)
        len_target = len_all if cf_mode == self.ALL else len(self.union_color_sets)

        for i in range(len_target):
            if isinstance(all_sets[i], ColorSet):
                if all_sets[i].color:
                    color = all_sets[i].color
                else:
                    color = self.colors[self.next_color_index]
                    ColorFields.next_color_index = (ColorFields.next_color_index + 1) % len_colors
                symbol = all_sets[i].symbol
            else:
                color = None
                symbol = all_sets[i]

            diff = Symbol('difference')
            diff.append(symbol)
            for j in range(i + 1, len_all):
                if isinstance(all_sets[j], ColorSet):
                    diff.append(all_sets[j].symbol)
                else:
                    diff.append(all_sets[j])

            if height:
                diff = Symbol('linear_extrude', height).add_others(diff)
            if color:
                diff = Symbol('color', color).add_others(diff)
            union.append(diff)
        """

        return union

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
