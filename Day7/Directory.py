from typing import List
from File import File

class Directory:
  def __init__(self, name: str):
    self.name: str = name
    self.directories: List[Directory] = list()
    self.files: List[File] = list()

  def getSize(self):
    sumOfFiles = sum([file.size for file in self.files])
    sumOfDirectories = sum([dir.getSize() for dir in self.directories])
    return sumOfFiles + sumOfDirectories