# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv
import os
import copy


class ConvertCsv:
    def __init__(self):
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        self.table = []

    def csv_to_table(self, file_name):
        self.table = []
        with open(os.path.join(self.__location__, file_name)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.table.append(dict(r))
        return self.table


converter = ConvertCsv()
converted_table = converter.csv_to_table('persons.csv')


# add in code for a Database class
class DataBase:
    def __init__(self):
        """Initialize an attribute named database, which will be used a lot"""
        self.database = []

    def insert(self, table):
        """Inserts table into the database object"""
        self.database.append(table)

    def search(self, table_name):
        """Find a table from the database which matches the name given"""
        for table in self.database:
            if table.table_name == table_name:
                return table

        return None


# add in code for a Table class
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        """
        Creates a joined table from the two with a common key
        """
        joined_table = Table(f"{self.table_name}_joins_{other_table}", [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        """
        Creates a filtered table which filters the items table to have certain
         condition

        """
        filtered_table = Table(f"{self.table_name}_filtered", [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    @staticmethod
    def __is_float(element):
        """
        check if the element give is float
        :param element:
        :return:
        """
        if element is None:
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def aggregate(self, function, aggregation_key):
        """
        Returns a values calculated by the given aggregation_key
        """
        temps = []
        for item1 in self.table:
            if self.__is_float(item1[aggregation_key]):
                temps.append(float(item1[aggregation_key]))
            else:
                temps.append(item1[aggregation_key])
        return function(temps)

    def select(self, attributes_list):
        """
        Returns a table that only have the given attributes from
        the attributes_list
        """
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    # new code added as a requirement
    def insert(self, new_dict):
        """
        Inserts new dict into table
        :param new_dict:
        :return:
        """
        self.table.append(new_dict)

    # new code added as a requirement
    def update(self, user_id, key_id, key, new_value):
        """
        Updates the value of a key indication
        :param key_id:
        :param user_id:
        :param key:
        :param new_value:
        :return:
        """
        for i in self.table:
            if i[key_id] == user_id:
                index = self.table.index(i)
                self.table[index][key] = new_value

    def __str__(self):
        return f"{self.table_name}: {str(self.table)}"

