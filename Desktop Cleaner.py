import shutil
import os
import time

print(os.system("time"))

os.mkdir("C 99/C 99 Example")

print(os.getcwd())

path="/Users/Akhil/Python/C 98/98.py"
exist=os.path.exists(path)
print(exist)

root=os.path.splitext(path)
print(root)

print(os.listdir())

dst=shutil.copy("C 98/98.py", "C 99")

dst=shutil.move("C 99/99 1.py", "C 98")
dst=shutil.move("C 99/99.py", "C 98")