def name_upper(name):
    """Имя пользователя с заглавных букв"""
    try:
        # Если имя из двух частей (имя/отчество)
        a, b = name.split()
        get_full_name = lambda a, b: a[0].upper() + a[1:].lower() + ' ' + b[0].upper() + b[1:].lower()
        return get_full_name(a, b)
    except ValueError:
        return name[0].upper() + name[1:].lower()