import inspect

def with_names(*items):
    frame = inspect.currentframe().f_back
    local_vars = frame.f_locals

    names = []
    for item in items:
        #Find var name
        for var_name, var_value in local_vars.items():
            if var_value is item:
                names.append(var_name)
                break

    return [list(items), names]
