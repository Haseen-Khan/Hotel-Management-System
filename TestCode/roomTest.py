import sys
sys.path.append("..")

import unittest
from unittest import mock
from Model.room import *



class roomTest(unittest.TestCase):
    dbc = mock.MagicMock()

    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc

    def fix_rows(self):
        rows = [{'id': 1, 'name': 'John'},
                {'id': 2, 'name': 'Jane'}, ]
        return rows

    def test_cursor_method(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows()
        #(rows, 'users', dbc)
        self.assertFalse(dbc.cursor.called)

    def test_on_databse_exception(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows()

        with dbc.cursor() as cursor:
            cursor.executemany.side_effect = Exception('Some DB error')



    def make_insert_statement(field_names, table_name):
        field_names_str = ', '.join(field_names)
        placeholder_str = ','.join('?' * len(field_names))
        insert_sql = f'INSERT INTO {table_name}({field_names_str}) VALUES ({placeholder_str})'
        return insert_sql


if __name__ == '__main__':
    unittest.main()
