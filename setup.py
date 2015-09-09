"""
Setup script for PWF.
"""

from setuptools import setup, find_packages


def read_file(path):
    with open(path) as f:
        return f.read()


version = read_file('version.txt')
readme = read_file('README.md')

setup(
    name='pwf',
    version=version,
    description=readme,
    url='https://github.com/kvas-it/pwf',
    author='Vasily Kuznetsov',
    author_email='kvas.it@gmail.com',
    license='MIT',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License'
    )
)

