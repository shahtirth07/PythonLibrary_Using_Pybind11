from setuptools import setup, Extension

setup(
    name='my_cleaning_package',
    version='0.1',
    ext_modules=[Extension('cleaning', sources=['cleaning.c'])],
    packages=['my_cleaning_package'],
    description='Data cleaning acceleration using C and ctypes.',
)
