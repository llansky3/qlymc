from setuptools import setup
from pathlib import Path
from git import Repo 

def get_version():
    repo = Repo(Path(__file__).parent.is_absolute())
    current_version = repo.git.show('--no-patch','--format=%ct.%h','HEAD')
    # path = Path(__file__).parent.resolve()
    # current_version = '0.1.0'
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
