import venv
import os
import subprocess
import sys

os.chdir(sys.path[0])

venv.create('.venv')

python_bin = './.venv/Scripts/python.exe'

subprocess.run([python_bin, '-m', 'ensurepip', '--default-pip'])
subprocess.run([python_bin, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.run([python_bin, '-m' 'pip', 'install', '-r', 'requirements.txt'])