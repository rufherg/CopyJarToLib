import os
import sys
import re
import argparse
import platform
import shutil
 
path ='F:\\Knownsec\\Environment\\WebLogic\\WebLogic_Home\\12.2.1.4.0'

JarRegex = re.compile( r'^.*\.jar$' )

class CopyJar():

    def __init__(self, target_path, copy_path=None):
        self.flag = self.get_os()
        self.base_path = os.getcwd()
        self.target_path = target_path
        self.default_path = self.base_path + self.flag + target_path.split(self.flag)[-1] + "_lib"
        self.copy_path = copy_path if copy_path != None else self.default_path

    @staticmethod
    def get_os():
        if platform.system() == 'Windows':
            return '\\'
        elif platform.system() == 'Darwin' or platform.system() == 'Linux':
            return '/'

    def copy(self, Filelist):
        try:
            print("[INFO]: Start copy jar file ...")
            if mkdir(self.copy_path):
                for file in Filelist:
                    shutil.copy(file, self.copy_path)
                print("[INFO]: All done")
        except Exception as e:
            print("[ERROR]: " + str(e))

    def run(self):
        print("-"*25 + " Scan JAR File " + "-"*25)
        file_list = get_filelist(self.target_path)
        for file in file_list:
            print("[INFO]: " + file)
        print("[INFO]: Total count " + str(len(file_list)))
        print("-"*65)
        print("-"*25 + " Copy JAR File " + "-"*25)
        self.copy(file_list)

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print("[INFO]: Path: " + path + " make success!")

        return True
    else:
        print("[ERROR]: Path: " + path + " already exist, please choose new path!")

        return False

def get_filelist(dir):
    Filelist = []
    for home, dirs, files in os.walk(path):
        for filename in files: 
            # 文件名列表，包含完整路径 
            if re.findall(JarRegex,filename):
                Filelist.append(os.path.join(home, filename)) 
                # 文件名列表，只包含文件名 
                # Filelist.append(filename) 

    return Filelist
 
if __name__ =="__main__":
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    parser = argparse.ArgumentParser(description='Copy Jar To Library',add_help=True)
    parser.add_argument('-t','--target',default=None,help='目标路径（需完整路径）',type=str)
    parser.add_argument('-c','--copy',default=None,help='复制路径（需完整路径）',type=str)
    args = parser.parse_args()

    if args.target:
        try:
            copy = CopyJar(args.target, args.copy)
            copy.run()
        except Exception as e:
            print("Something ERROR!")
            print("[ERROR]: " + str(e))
            exit()