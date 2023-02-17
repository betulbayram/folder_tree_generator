import os

class Generator:
    def __init__(self):
        self.tree_path = "C:/Users//betul//Documents//CPP" #TODO
        self.dirs = os.listdir(self.tree_path)
        self.file = open("tree.txt", "w")
        self.ignore = [".exe", ".git", ".gitignore", ".vscode"]
        self.counter = 1
        self.flag = 0
        self.flag2 = 0
    def write_to_txt(self, base, files):
        base = base.split("\\")[-1]
        self.file.write("\n" + (self.counter) * "\t" + "|*** " +  base)
        for f in files:
            self.flag2 = 0
            for sub in self.ignore:
                if sub in f:
                    self.flag2 = 1
                    continue
            if self.flag2 == 0:
                self.file.write("\n" +( self.counter + 1) * "\t" +  "|-- "+ f) 


    def generate(self):
        roots = []
        for root, dirs, files in os.walk(self.tree_path):
            self.flag = 0
            for sub in self.ignore:
           
                if root.find(sub) != -1:
                    self.flag = 1
                    continue
            if(self.flag == 0):

                
                if self.counter == 1:
                    self.write_to_txt(root.split("//")[-1], files)
                else:
                    self.counter = len(root.split("\\"))
                    self.write_to_txt(root.split("\\")[-1], files)

            self.counter = self.counter + 1

if __name__ == "__main__":

    g = Generator()
    g.generate()
