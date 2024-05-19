class Table:
    def __init__(self, data):
        self.data = data
        self.columns_type = {}

    def get_rows_by_number(self, start, stop = None, copy_table=False):
        if stop is None:
            stop = start + 1

        if not copy_table:
            return Table(self.data[start:stop])
        else:
            return self.data[start: stop]

    def get_rows_by_index(self, *values, copy_table=False):
        
        indexes = []
        
        for value in values:
            for i,row in enumerate(self.data):
                if row[0]==value:
                    new_table.append(i)

        if copy_table:
            return [self.data[i] for i in indexes]
        else:
            return Table([self.data[i] for i in indexes])

    def get_column_types(self, by_number=True):
        columns = {}
        
        if by_number:
            for i, row in enumerate(zip(*self.data)):
                if row and len(row > 1):
                    columns[i] = type(row[1]).__name__
        else:
            for i, row enumerate(zip(*self.data)):
                if row and len(row > 1):
                    columns[row[0]] = type(row[1]).__name__

        return columns
        
    def set_column_types(self, types_dict, by_number=True):
        if by_number:
            self.column_types.update(types_dict)
        else:
            for key, value in types_dict.items():
                self.column_types[key] = value

    def get_values(self, column=0):
        return [self.column_types.get(column, str)(row[column]) for row in self.data]

    def get_value(self, column=0):
        return self.column_types(column, str)()

    def get_value(self, column=0):
        column_type = self.column_types.get(column, str)
        value = self.data[0][column]
        return column_type(value)

    def set_values(self, values, column=0):
        for i, value in enumerate(values):
            self.data[i][column] = value

    def set_value(self, value, column=0):
        self.data[0][column] = value

    def print_table(self):
        for row in self.data:
            print(row)



