def param_dict(cls_obj):
    import inspect
    members = inspect.getmembers(cls_obj)
    for member in members:
        if '__dict__' in member:
            param_grid = member[1]
            return param_grid