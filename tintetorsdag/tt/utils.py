from datetime import date
import os


def is_thursday():
    return date.today().weekday() == 3 or os.getenv("IS_THURSDAY", "").lower() in [
        "y",
        "yes",
        "1",
        "t",
        "true",
    ]
