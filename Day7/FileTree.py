from typing import List, Tuple
from Directory import Directory

class FileTree:
  def __init__(self, root: Directory):
    self.tree = [root]
    self.currentIndex = 0

  def rootDirectory(self):
    return self.tree[0]

  def currentDirectory(self):
    return self.tree[self.currentIndex]

  def traverseToRoot(self):
    self.tree = self.tree[:1]
    self.currentIndex = 0

  def traverseToParent(self):
    self.tree.pop()
    self.currentIndex -= 1

  def traverseToChild(self, name: str):
    childDir = next((dir for dir in self.currentDirectory().directories if dir.name == name), None)
    if childDir != None:
      self.tree.append(childDir)
      self.currentIndex += 1

  def getRecursiveSizes(self, directory: Directory) -> List[int]:
    sizes = []
    for dir in directory.directories:
      sizes.extend(self.getRecursiveSizes(dir))
    
    sizes.append(directory.getSize())
    return sizes

  def getRecursiveSummaries(self, directory: Directory) -> List[Tuple[str, int]]:
    sizes = []
    for dir in directory.directories:
      sizes.extend(self.getRecursiveSummaries(dir))
    
    sizes.append((directory.name, directory.getSize()))
    return sizes

  def getTotalSize(self, upperThreshold: int = 0):
    dirSizes = self.getRecursiveSizes(self.tree[0])
    return sum(filter(lambda size: size <= upperThreshold, dirSizes))