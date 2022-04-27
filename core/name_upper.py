def name_upper(name):
    """Имя пользователя с заглавных букв"""
    try:
        # Если имя из двух частей (имя/отчество)
        a, b = name.split()
        return a[0].upper() + a[1:].lower() + ' ' + b[0].upper() + b[1:].lower()
    except ValueError:
        return name[0].upper() + name[1:].lower()
