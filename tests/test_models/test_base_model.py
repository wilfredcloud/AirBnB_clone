#!/usr/bin/python3
"""
Defines unittests for BaseModel

Unitest classes:
    TestBaseModel_initialization
    TestBaseModel_save
    TestBaseModel_to_dict
    TestBaseModel_str_representation
"""
from models.base_model import BaseModel
from time import sleep
from datetime import datetime
import unittest


class TestBaseModel_initialization(unittest.TestCase):
    """Unit tests to BaseModel Initialization"""

    def test_default_init(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_two_model_unique_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_updated_at_and_created_at_are_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_two_models_create_at_are_different(self):
        bm1 = BaseModel()
        sleep(0.01)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    # def test_init_model_from_kwargs(self):
    #    bm = BaseModel()
    #    bm_dict = bm.to_dict()
    #    new_bm = BaseModel(bm_dict)
    #    self.assertEqual(BaseModel, type(new_bm))
    #    #self.assertEqual(bm.id, new_bm.id)
    #    self.assertEqual(bm.created_at, new_bm.created_at)
    #    self.assertEqual(bm.updated_at, new_bm.updated_at)

    def test_init_model_from_know_kwargs(self):
        dt_iso = datetime.today().isoformat()
        bm = BaseModel(id="2410", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "2410")
    #    self.assertEqual(bm.created_at, dt_iso)
    #    self.assertEqual(bm.updated_at, dt_iso)


class TestBaseModel_save(unittest.TestCase):
    """Unit tests for BaseModel save"""

    def test_model_upated_at_changed(self):
        base_model = BaseModel()
        init_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(init_updated_at, base_model.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unit tests for BaseModel to dict"""

    def test_model_to_dict_has_all_key(self):
        bm_dict = BaseModel().to_dict()
        self.assertIn("__class__", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("id", bm_dict)

    def test_model_to_dict__class__equal_class_name(self):
        bm_dict = BaseModel().to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")


class TestBaseModel_str_representation(unittest.TestCase):
    """Unit test to test string representation of BaseModel"""

    def test_class_name_str_representation(self):
        self.assertIn("[BaseModel]", BaseModel().__str__())


if __name__ == "__main__":
    unittest.main()
