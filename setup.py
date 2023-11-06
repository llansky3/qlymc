from setuptools import setup

setup(
    name='qlymc',
    version='0.1.0',
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
