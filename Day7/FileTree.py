from Directory import Directory

class FileTree:
  def __init__(self, root: Directory):
    self.tree = [root]
    self.currentIndex = 0

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

  def getRecursiveSizes(self, directory: Directory):
    sizes = []
    for dir in directory.directories:
      sizes.extend(self.getRecursiveSizes(dir))
    
    sizes.append(directory.getSize())
    return sizes


  def getTotalSize(self, upperThreshold: int = 0):
    self.traverseToRoot()

    dirSizes = self.getRecursiveSizes(self.currentDirectory())
    return sum(filter(lambda size: size <= upperThreshold, dirSizes))