import re

def validate_user(user):
    pattern = r"[a-zA-Z0-9]{4,10}"
    user_pattern = re.compile(pattern)
    match = user_pattern.fullmatch(user)
    if match:
        return True
    else:
        print("Usuario inválido. Puede contener letras mayúsculas, minúsculas y números con una longitud entre 4 y 10.")
        return False

def validate_accesskey(accesskey):
    pattern = r"[0-9]{8}"
    password_pattern = re.compile(pattern)
    match = password_pattern.fullmatch(accesskey)
    if match:
        return True
    else:
        print("Clave inválida. Tienen que ser 8 dígitos.")
        return False

def validate_age(age):
    pattern = r"^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$"
    age_pattern = re.compile(pattern)
    match = age_pattern.fullmatch(age)
    if match:
        return True
    else:
        print("Fecha introducida inválida. Formato dd/mm/yyyy.")
        return False

def validate_phone(phone):
    pattern = r"^[0-9]{9}"
    phone_pattern = re.compile(pattern)
    match = phone_pattern.fullmatch(phone)
    if match:
        return True
    else:
        print("Teléfono introducido inválido.")
        return False

def validate_id(id):
    pattern = r"^(\d{8})([A-Z])$"
    id_pattern = re.compile(pattern)
    match = id_pattern.fullmatch(id)
    if match:
        return True
    else:
        print("Documento de identidad introducido inválido.")
        return False
