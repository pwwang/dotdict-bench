from typing import Any


def format_doc(obj: Any = None, **kwargs: Any) -> Any:
    """Format the docstr"""
    if obj is None:
        return lambda o: format_doc(o, **kwargs)

    obj.__doc__ = obj.__doc__.format(**kwargs)
    return obj
