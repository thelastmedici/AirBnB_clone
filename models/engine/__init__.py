#!/usr/bin/python3
'''import all necesarry modules'''
from models.engine import file_storage


storage = file_storage.FileStorage() # an instance of FileStorage class
storage.reload()
