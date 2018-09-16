from data_types import *
import types


def pr_str(ds, print_readably=True):
    if isinstance(ds, list):
        return f"({' '.join(pr_str(d) for d in ds)})"
    elif isinstance(ds, types.FunctionType):
        return "#<function>"
    elif isinstance(ds, bool):
        return 'true' if ds else 'false'
    else:
        return str(ds)