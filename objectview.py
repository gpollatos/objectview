class ObjectView(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectView, self).__init__(**kwargs)
        for arg in args:
            if not arg:
                continue
            elif isinstance(arg, dict):
                for key, val in arg.items():
                    self[key] = val
            else:
                raise TypeError()
        for key, val in kwargs.items():
            self[key] = val

    def __setattr__(self, key, value):
        if not hasattr(ObjectView, key):
            self[key] = value
        else:
            raise

    def __setitem__(self, name, value):
        value = ObjectView(value) if isinstance(value, dict) else value
        super(ObjectView, self).__setitem__(name, value)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __getitem__(self, name):
        if name not in self:
            self[name] = {}
        return super(ObjectView, self).__getitem__(name)

    def __delattr__(self, name):
        del self[name]
