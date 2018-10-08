import re
from data_types import *
import types

str_map = {
    '"': '\\"',
    "\n": "\\n" ,
    "\\": "\\\\"
}


def format_string(ds):
   return ''.join(str_map.get(char, char) for char in str(ds))


def pr_str(ds, print_readably=True):

    if isinstance(ds, list):
        return f"({' '.join(pr_str(d, print_readably) for d in ds)})"

    elif isinstance(ds, types.FunctionType):
        return "#<function>"

    elif isinstance(ds, Bool):
        return 'true' if ds else 'false'
    
    elif isinstance(ds, String):
        if print_readably:
            return f'"{format_string(ds)}"'
        else:
            return f'{ds}'

    else:
        return str(ds)
