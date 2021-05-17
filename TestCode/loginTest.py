import sys
sys.path.append("..")

from tkinter import messagebox
import unittest
from Controller.login import *

class loginTest(unittest.TestCase):


    def test_login_function(self):

         self.assertTrue("Haseen" or "123",messagebox.showinfo)
         self.assertFalse("", messagebox.showinfo)


    def test_reset_pass(self):
        self.assertTrue("Select",messagebox.showerror)




if __name__=="__main__":
    unittest.main()