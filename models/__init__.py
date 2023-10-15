#!/usr/bin/python3

"""
Create unique FileStorage instance for the application

"""
import importlib


FileStorage = importlib.import_module('models.engine.file_storage').FileStorage

storage = FileStorage()
storage.reload()
