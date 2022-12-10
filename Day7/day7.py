from FileTree import FileTree
from Directory import Directory
from File import File

def isDirectory(text: str):
  return "dir" in text

def extractDirectory(text: str) -> Directory:
  return Directory(text.split(" ")[1])

def isFile(text: str):
  try:
    int(text.split(" ")[0])
    return True
  except ValueError:
    return False

def extractFile(text: str) -> File:
  info = text.split(" ")
  return File(info[1], int(info[0]))

def isDirectoryChange(text: str):
  return "cd" in text

fileTree = FileTree(Directory("/"))

with open('./Day7/input.txt') as file:
  for line in file:
    line = line.strip()

    if isDirectory(line):
      fileTree.currentDirectory().directories.append(extractDirectory(line))
    elif isFile(line):
      fileTree.currentDirectory().files.append(extractFile(line))
    elif isDirectoryChange(line):
      if ".." in line:
        fileTree.traverseToParent()
      else:
        fileTree.traverseToChild(line.split(" ")[2])

upperThreshold = 100000
print(f"Upper threshold: {upperThreshold}\nTotal size: {fileTree.getTotalSize(upperThreshold)}")