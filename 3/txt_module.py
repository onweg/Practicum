def save_table(nameFile, data):
    try:
        with open(nameFile, 'w') as file:
            file.writelines("\t".join(row) for row in data)
            
    except FileNotFoundError:
        raise Exception("Файл не найден")

