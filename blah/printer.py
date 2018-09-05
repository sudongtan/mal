from data_types import *

def pr_str(ds):
    if isinstance(ds, Symbol):
        return ds.name
    elif isinstance(ds, Integer):
        return ds.string_value
    else:
        return f"({' '.join(pr_str(d) for d in ds)})"