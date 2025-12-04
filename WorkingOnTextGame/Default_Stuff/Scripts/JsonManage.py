def ClassToJson(cls):
    data = {}
    for key, value in vars(cls).items():
        if key.startswith("__"): continue
        if isinstance(value, type):
            data[key] = ClassToJson(value)
        elif callable(value):
            continue
        else:
            data[key] = value
    return data

def JsonToClass(data, cls):
    for key, value in data.items():
        if hasattr(cls, key):
            attr = getattr(cls, key)
            if isinstance(value, dict) and isinstance(attr, type):
                JsonToClass(value, attr)
            else:
                setattr(cls, key, value)