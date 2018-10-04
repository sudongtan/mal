import re
from data_types import *
import types


def pr_str(ds, print_readably=True):
    if isinstance(ds, list):
        return f"({' '.join(pr_str(d) for d in ds)})"

    elif isinstance(ds, types.FunctionType):
        return "#<function>"

    elif isinstance(ds, Bool):
        return 'true' if ds else 'false'
    
    # elif isinstance(ds, Symbol):
    #     return str(ds)

    elif isinstance(ds, String):
        if print_readably:
            # print(ds, type(ds), len(ds))
            # print(str(ds), len(str(ds)))
            # print(len(str(ds).replace('\\', r'\\')))
            #print(ds.value, str(ds), re.escape(str(ds)))
            #print(ds.value, len(ds.value), str(ds))
            reps = [
                ('\\', r'\\'),
                ('"', r'\"'),
                ('\n', '\\n'),
            ]
            s = str(ds)
            for orig, new in reps:
                s = s.replace(orig, new)
                #print(s, len(s))
            return f'"{s}"'
            #print(ds.value, len(ds.value))
            #return '"' + re.escape(str(ds)).replace('\\ ', ' ')
        else:
            return '"' + str(ds) + '"'

    else:
        return str(ds)