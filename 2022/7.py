input_path = "input/7.txt"

class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.childs = []

    def appendFile(self, size):
        self.size += size

    def appendFolder(self, folder):
        self.childs.append(folder)

    def getParent(self):
        return self.parent

    def getSize(self):
        size = self.size
        cum = 0
        for child in self.childs:
            child_size, child_cum = child.getSize()
            size += child_size
            cum += child_cum

        if size <= 100000:
            return size, cum + size
        else:
            return size, cum

    def getFoldersWithMinSize(self, min_size):
        size = self.size
        folders = {}
        for child in self.childs:
            child_size, child_folders = child.getFoldersWithMinSize(min_size)
            size += child_size
            folders.update(child_folders)

        if size >= min_size:
            folders[size] = self

        return size, folders

def a():
    res = 0
    with open(input_path) as file:
        root_folder = Folder("/", None)
        current_folder = root_folder
        for line in file:
            line_stripped = line.strip()
            parts = line_stripped.split()
            if parts[0] == "$" and parts[1] == "cd":
                if parts[2] == "..":
                    current_folder = current_folder.getParent()
                else:
                    new_folder = Folder(parts[2], current_folder)
                    current_folder.appendFolder(new_folder)
                    current_folder = new_folder
            elif parts[0].isnumeric():
                current_folder.appendFile(int(parts[0]))
        res = root_folder.getSize()[1]
    return res


def b():
    res = 0
    with open(input_path) as file:
        root_folder = Folder("/", None)
        current_folder = root_folder
        for line in file:
            line_stripped = line.strip()
            parts = line_stripped.split()
            if parts[0] == "$" and parts[1] == "cd":
                if parts[2] == "..":
                    current_folder = current_folder.getParent()
                else:
                    new_folder = Folder(parts[2], current_folder)
                    current_folder.appendFolder(new_folder)
                    current_folder = new_folder
            elif parts[0].isnumeric():
                current_folder.appendFile(int(parts[0]))
        overall_size = root_folder.getSize()[0]
        needed_size = 30000000 - (70000000 - overall_size)
        print(needed_size)
        folders = root_folder.getFoldersWithMinSize(needed_size)[1]
        print(folders.keys())
        res = min(folders.keys())

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
