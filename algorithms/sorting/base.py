def args_validator(function):
    def wrapper(iterable, reverse=False):
        if iterable is None:
            raise ValueError('"iterable" cannot be NoneType')
        if not isinstance(reverse, bool):
            raise ValueError('"reverse" must be boolean')
        if len(iterable) < 2:
            return iterable
        else:
            return function(iterable, reverse)
    return wrapper
