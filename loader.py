

def get_settings():
    try:
        from settings import CONFIG
    except ImportError:
        from settings_example import CONFIG

    return CONFIG

def get_students():
    try:
        from students import userslist
    except ImportError:
        from students_example import userslist

    return userslist


