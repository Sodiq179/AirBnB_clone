#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
Module BaseModel
Parent class to all other classes
"""


class BaseModel():
  """Base class for Airbnb console clone project
  Methods:
    __init__(self, *args, **kwargs)
    __str__(self)
    __save(self)
    __repr__(self)
    to_dict(self)
    """

  def __init__(self, *args, **kwargs):
    """
    Attributes: 
      id: unique id, 
      created_at : Date of class creation
      Updated_at : Date of class last update
    """
    if kwargs:
      for key, val in kwargs.items():
        if "__class__" == key:
          pass
        elif "updated_at" == key:
          self.updated_at = datetime.strptime(kwargs["updated_at"],
                          "%Y-%m-%dT%H:%M:%S.%f")
        elif "created_at" == key:
          self.created_at = datetime.strptime(kwargs["created_at"],
                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
          setattr(self, key, val)
    else:
      self.id = str(uuid4())
      self.created_at = datetime.now()
      self.updated_at = datetime.now()
      models.storage.new(self)

  def __str__(self):
    """
    Returns the class info in string format
    """
    return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

  def __repr__(self):
    """
    String representation of the class
    """
    return (self.__str__())

  def save(self):
    """
    Updates the instance time
    """
    self.updated_at = datetime.now()
    models.storage.save()

  def to_dict(self):
    """
    Return dic with string formats of times; add class info to dic
    """
    dictRep = {}
    dictRep["__class__"] = self.__class__.__name__
    for key, value in self.__dict__.items():
      if isinstance(value, (datetime, )):
        dictRep[key] = value.isoformat()
      else:
        dictRep[key] = value
    return dictRep