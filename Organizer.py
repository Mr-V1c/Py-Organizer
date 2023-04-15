#!/bin/python3
import os
import sys
import re

print("sys is not implemnted yet, args:", len(sys.argv))


def main():
    os.chdir(os.environ["HOME"] + "/Downloads")
    os.system("ls -F > .OrganizerTMPfile")

    with open(".OrganizerTMPfile") as f:
        strlist = f.read().split("\n")[:-1]
        fList = []
        dirList = []

        for line in strlist:
            if line.endswith("/"):
                dirList.append(line[:-1])
            else:
                fList.append(line)

        for file in fList:
            ext = GetFileExt(file)
            dirName = FromExtGetDirName(ext)
            if HasDirNameInDirlist(dirName, dirList):
                MoveFileToDir(file, dirName)
            else:
                CreateDirAndAddFile(dirName, file)

    os.system("rm .OrganizerTMPfile")


def GetFileExt(file):
    objWithExt = re.search(r"\.(\w+)*$", file)
    try:
        assert objWithExt is not None
        filteredExt = objWithExt.group()[1:]
        return filteredExt

    except:
        return "No Extension"


def FromExtGetDirName(ext):
    directoryName = f"{ext} files".lower()
    return directoryName


def HasDirNameInDirlist(dirName, dirList):
    return dirName in dirList


def MoveFileToDir(file, dirName):
    os.system(f'mv "{file}" "{dirName}"')


def CreateDirAndAddFile(dirName, file):
    os.mkdir(dirName)
    MoveFileToDir(file, dirName)


main()
