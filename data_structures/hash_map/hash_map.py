"""
HashMap (Hash table)
Complexity:
    Algorithm	Average	 Worst case
    Search		O(1)	 O(n)
    Insert		O(1)	 O(n)
    Delete		O(1)	 O(n)

Sources: https://en.wikipedia.org/wiki/Hash_table
"""

from typing import Any, Iterable, Union


class HashMapItem:
    def __init__(self, key: Union[str, int], value: Any) -> None:
        self._key = key
        self.value = value

    @property
    def key(self) -> Union[str, int]:
        return self._key

    def __repr__(self) -> str:
        return f'<HashMapItem: ({self._key}: {self.value})>'

    def __str__(self) -> str:
        return f'({self._key}: {self.value})'


class HashMap:
    def __init__(self, size: int) -> None:
        self._size = size
        self._table = [None] * size

    def _hash_function(self, key: Union[str, int]) -> int:
        _hash = 0
        for i, c in enumerate(str(key)):
            _hash += ord(c) * i
        return _hash % self._size

    def __getitem__(self, key: Union[str, int]) -> Any:
        _initial_hash = _hash = self._hash_function(key)
        while self._table[_hash] is not None:
            if self._table[_hash] != -1:
                if self._table[_hash].key == key:
                    return self._table[_hash].value

            _hash += 1
            _hash %= self._size

            if _hash == _initial_hash:
                break
        raise KeyError(f'Key not found: {key}')

    def __setitem__(self, key: Union[str, int], value: Any) -> None:
        _initial_hash = _hash = self._hash_function(key)
        while self._table[_hash] is not None and self._table[_hash] != -1:
            if self._table[_hash].key == key:
                self._table[_hash].value = value
                return

            _hash += 1
            _hash %= self._size

            if _hash == _initial_hash:
                raise NotEnoughCells(
                    f'There is no place for this item: {self._table[_hash]}')
        self._table[_hash] = HashMapItem(key, value)

    def __delitem__(self, key: Union[str, int]) -> None:
        _initial_hash = _hash = self._hash_function(key)
        while self._table[_hash] is not None:
            if self._table[_hash] != -1:
                if self._table[_hash].key == key:
                    self._table[_hash] = -1
                    return

            _hash += 1
            _hash %= self._size

            if _hash == _initial_hash:
                break
        raise KeyError(f'Key not found: {key}')

    def __iter__(self) -> Iterable[HashMapItem]:
        for item in self._table:
            yield item

    def __contains__(self, key: Union[str, int]) -> bool:
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __repr__(self) -> str:
        return f'<HashMap: {[str(_) for _ in self]}>'

    def __str__(self) -> str:
        return f'{[str(_) for _ in self]}'


class NotEnoughCells(Exception):
    pass
