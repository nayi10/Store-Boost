
from cx_Freeze import setup, Executable
target = Executable(
    script="setup.py",
    base="Win32GUI",
    icon="favicon.ico"
    )

setup(
      name="Inventory Management System",
      version='1.0.0',
      author='Bandughana',
      description='Bandughana Inventory Management System',
      executables = [target])
