from setuptools import setup
from git import Repo 

def get_version():
    repo = Repo('.')
    current_version = repo.git.show('--no-patch','--format=%ct.%h','HEAD')
    return current_version

setup(
    name='qlymc',
    version=get_version(),
    description='Framework for gathering software quality metrics',
    url='https://github.com/llansky3/qlymc',
    author='Lukas Lansky',
    author_email='lukas.lansky@suse.com',
    license='GPL-2.0',
    packages=['qlymc'],
    entry_points={
        'console_scripts': ['qlymc=qlymc.__main__:main']
    }
)
