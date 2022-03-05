import os
print(os.system("date"))

os.mkdir("C 99/C 99 Example")

print(os.getcwd())

path="/Users/Akhil/Python/C 98/98.py"
exist=os.path.exists(path)
print(exist)

root=os.path.splitext(path)
print(root)

print(os.listdir())

import shutil
dst=shutil.copy("C 98/98.py", "C 99")

dst=shutil.move("C 99/98 copy.py", "C 98")