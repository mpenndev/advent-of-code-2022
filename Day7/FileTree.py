from Directory import Directory

class FileTree:
  def __init__(self, root: Directory):
    self.root = root
    self.currentDirectory = root

  def traverseToRoot(self):
    self.currentDirectory = self.root
    self.parentDirectory = None

  def traverseToParent(self):
    self.currentDirectory = self.parentDirectory

  def traverseToChild(self, name: str):
    childDir = next((dir for dir in self.currentDirectory.directories if dir.name == name), None)
    if childDir != None:
      self.parentDirectory = self.currentDirectory
      self.currentDirectory = childDir