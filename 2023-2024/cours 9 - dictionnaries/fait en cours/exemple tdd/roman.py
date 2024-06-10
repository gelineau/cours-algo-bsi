def to_roman(arabic_number: int) -> str:
    if arabic_number < 0:
        raise ValueError("Romans did not know negative numbers")
    return "I" * arabic_number
