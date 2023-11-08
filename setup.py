from setuptools import setup

def get_version():
    with open('version.txt') as f:
        current_version =  f.readline()
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
