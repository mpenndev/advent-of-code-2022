from typing import List
from File import File

class Directory:
  def __init__(self, name: str):
    self.name = name
    self.directories = list()
    self.files = list()

  def getSize(self):
    sumOfFiles = sum([file.size for file in self.files])
    sumOfDirectories = sum([dir.getSize() for dir in self.directories])
    return sumOfFiles + sumOfDirectories