import unittest
from models.base import Base
"""unittest base class"""


class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset the __nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_base_id_none(self):
        """Test creating a Base instance with id=None"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_id_provided(self):
        """Test creating a Base instance with a specific id"""
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_base_id_mixed(self):
        """Test creating Base instances with and without id"""
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 15)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """Test converting a list of dictionaries to a JSON string"""
        list_dicts = [{'id': 1}, {'id': 2}]
        json_str = Base.to_json_string(list_dicts)
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[{"id": 1}, {"id": 2}]')

    def test_to_json_string_none(self):
        """Test converting None to a JSON string"""
        json_str = Base.to_json_string(None)
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[]')

    def test_to_json_string_empty(self):
        """Test converting an empty list to a JSON string"""
        json_str = Base.to_json_string([])
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[]')

    def test_from_json_string(self):
        """Test converting a JSON string to a list of dictionaries"""
        json_str = '[{"id": 1}, {"id": 2}]'
        list_dicts = Base.from_json_string(json_str)
        self.assertIsInstance(list_dicts, list)
        self.assertEqual(list_dicts, [{'id': 1}, {'id': 2}])

    def test_from_json_string_none(self):
        """Test converting None to an empty list"""
        list_dicts = Base.from_json_string(None)
        self.assertIsInstance(list_dicts, list)
        self.assertEqual(list_dicts, [])

    def test_from_json_string_empty(self):
        """Test converting an empty string to an empty list"""
        list_dicts = Base.from_json_string("")
        self.assertIsInstance(list_dicts, list)
        self.assertEqual(list_dicts, [])

    def test_create(self):
        """Test creating an instance from a dictionary"""
        dictionary = {'id': 1}
        base_instance = Base.create(**dictionary)
        self.assertEqual(base_instance.id, 1)

    def test_load_from_file_no_file(self):
        """Test loading instances from a non-existent file"""
        instances = Base.load_from_file()
        self.assertIsInstance(instances, list)
        self.assertEqual(instances, [])

if __name__ == '__main__':
    unittest.main()
