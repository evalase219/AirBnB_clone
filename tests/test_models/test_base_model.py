#!/usr/bin/python3
"""Define unittests for base_model.py
"""
import unittest
from models.basemodel import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Unittest for testing the parent class BaseModel"""

    def test_no_args(self):
        """Checks if BaseModel is instantiated without arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_if_id_is_str(self):
        """Test if the public instant attribute id is a string."""
        self.assertEqual(str, type(BaseModel().id))

    def test_if_created_at_is_datetime(self):
        """Test if the public instant attribute created_at is a datetime."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_if_updated_at_is_datetime(self):
        """Test if the public instant attribute updated_at is a datetime."""
        self.assertEqual(datetime, type(BaseModel().updated_at))
    
    def test_objects_ids_are_not_equal(self):
        """Check if two different object ids are not equal"""
        object_id_1 = 1234567890
        object_id_2 = 9876543210
        self.assertNotEqual(object_id_1, object_id_2)

    def test_instances_of_BaseModel_not_equal(self):
        """Check if two instances of BaseModel are not equal"""
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1, base_model_2)

    def test_basemodel_is_from_object_class(self):
        """Check if the basemodel originates from object class"""
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model, object))

    def test_basemodel_string_format(self):
        """Check if the expected model is in the string format."""
        bm = BaseModel()
        exp_str = f"[{bm.__class__.__name__}] ({bm.id}) {bm.__dict__}"
        act_str = str(bm)
        self.assertEqual(exp_str, act_str)

    def test_created_at_updated_at_inequality(self):
        """Inequality of created_at and updated_at after save method"""
        base_model = BaseModel()
        base_model.save()
        created_at = base_model.created_at
        updated_at = base_model.updated_at
        self.assertLess(created_at, updated_at)

    def test_created_time_less_than_current_time(self):
        """Check if the created time is less than the current time"""
        current_time = datetime.datetime.now()
        created_time = datetime.datetime(2023, 10, 13, 12, 0, 0)
        self.assertLess(created_time, current_time)
    
    def test_updated_at_inequality(self):
        """Check the equality of updated_at after or before save"""
        base_model = BaseModel()
        updated_at_before_save = base_model.updated_at
        base_model.save()
        updated_at_after_save = base_model.updated_at
        self.assertGreater(updated_at_after_save, updated_at_before_save)
    
    def test_id_is_valid_uuid4_len_36(self):
        """Check if an id is a valid UUID4 string with a length of 36"""
        id = "123e4567-e89b-12d3-a456-426655440000"
        self.assertTrue(is_uuid4_len_36(id))
    
    def test_created_at_updated_at_iso_format(self):
        """Check if created_at and updated_at are in iso format"""
        to_dict_result = {
            "created_at": "2023-10-14T22:55:45.123456",
            "updated_at": "2023-10-14T22:55:45.123456"
            }
        self.assertTrue(check_created_at_updated_at_iso_format(to_dict_result))
if __name__ == "__main__":
    unittest.main()
