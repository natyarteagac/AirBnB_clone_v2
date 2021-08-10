#!/usr/bin/python3
""" Testing of console """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class test_console(unittest.TestCase):
    """Testing"""

    def test_do_create(self):
        """ Testing do create of console"""
        # Returning the console string's output as variable
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            state_id = f.getvalue()
            self.assertTrue(len(state_id) >= 1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            state_id = f.getvalue()
            self.assertTrue("** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f2:
            HBNBCommand().onecmd("create State name=Natalia")
            state_id_two = f2.getvalue()
            self.assertNotEqual(state_id_two, state_id)
