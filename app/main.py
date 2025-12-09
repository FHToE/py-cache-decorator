from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def get_key_by_args(*args, **kwargs) -> str:
        cache_key = ""
        for arg in args:
            cache_key += str(arg)
        for key, value in kwargs.items():
            cache_key += f"{str(key)}{str(value)}"

        return cache_key

    def inner(*args, **kwargs) -> Any:
        cache_key = get_key_by_args(*args, **kwargs)

        if cache_dict.get(cache_key) is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
        else:
            print("Getting from cache")

        return cache_dict[cache_key]

    return inner
