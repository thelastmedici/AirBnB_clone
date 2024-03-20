#!/usr/bin/python3
import uuid
import datetime

"""import all necesarry modules"""


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """__init__ method of BaseModel class
        Args:
            args (tuple): arguments
            kwargs (dict): key word arguments
        """
        if kwargs:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, value) 

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """A string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """update updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dict of the BaseModel instance.
         includes key/value pair and '__class__' representing
         the class name of the object
           """
        base_dict = dict(self.__dict__)
        base_dict['__class__'] = type(self).__name__
        base_dict['created_at'] = base_dict['created_at'].isoformat()
        base_dict['updated_at'] = base_dict['updated_at'].isoformat()
        return base_dict