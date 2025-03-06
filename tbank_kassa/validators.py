from typing import Sequence

from pydantic import AfterValidator


def validate_length(max_length: int):
    def wrapped(value: Sequence):
        if len(value) > max_length:
            msg = f'Поле не может содержать больше {max_length} элементов.'
            raise ValueError(msg)
        return value

    return AfterValidator(wrapped)
