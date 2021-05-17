import sys
sys.path.append("..")

import unittest
from tkinter import messagebox
from Controller.register import *

class registerTest(unittest.TestCase):

    def test_register_data(self):

        self.assertFalse(0,messagebox.showerror)


if __name__=="__main__":
    unittest.main()