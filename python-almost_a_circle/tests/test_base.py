import unittest
from models.base import Base
"""unittest base class"""


class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset the __nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_base_auto_id(self):
        """Test for automatically assigned IDs"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_base_custom_id(self):
        """Test for custom ID assignment"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_base_auto_id_after_custom(self):
        """Test for automatic ID assignment after a custom ID"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string_none(self):
        """Test JSON string conversion for None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test JSON string conversion for empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test JSON string conversion for a valid list of dictionaries"""
        dict_list = [{'id': 12}, {'id': 34}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 12}, {"id": 34}]')
        self.assertIsInstance(json_str, str)

    def test_from_json_string_none(self):
        """Test conversion from JSON string when None is provided"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self):
        """Test conversion from JSON string for empty list"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        """Test conversion from JSON string for a valid JSON string"""
        json_str = '[{"id": 89}, {"id": 90}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, [{"id": 89}, {"id": 90}])
        self.assertIsInstance(dict_list, list)

    def test_save_to_file(self):
        """Test saving list of Base objects to a file"""
        b1 = Base(1)
        b2 = Base(2)
        list_objs = [b1, b2]
        Base.save_to_file(list_objs)
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(Base.from_json_string(content), [{'id': 1}, {'id': 2}])

    def test_load_from_file_no_file(self):
        """Test loading from a file that does not exist"""
        self.assertEqual(Base.load_from_file(), [])

    def test_load_from_file(self):
        """Test loading list of Base objects from a file"""
        b1 = Base(1)
        b2 = Base(2)
        list_objs = [b1, b2]
        Base.save_to_file(list_objs)
        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

if __name__ == '__main__':
    unittest.main()
