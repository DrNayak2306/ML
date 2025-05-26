import os

# use of - option
os.system("echo \"print('- option demo')\" | python3 -")

# make a custom package to demonstrate usage of -m option
createPackage = "mkdir myPackage 2> /dev/null; touch myPackage/__init__.py 2> /dev/null"
hiModule = """def hiFn(): print('Hi from package')
if __name__ == '__main__': hiFn()
"""
createModule = f"echo \"{hiModule}\" > myPackage/hiModule.py"
callModule = "python3 -m myPackage.hiModule"
demo = [createPackage, createModule, callModule]

for i in demo:
    try:
        os.system(i)
    except:
        pass

# use of -c option
os.system("python3 -c \"print('-c option demo')\"")