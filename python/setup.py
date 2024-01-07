from setuptools import find_packages, setup

setup(
    name='x3dh',
    packages=find_packages(include=['x3dh']),
    version='0.0.1',
    description='Embeded the xxxdh, which iplementation of the Extended Triple Diffie-Hellman key exchange protocol written in Rust, on Python. xxxdh is written by Olexander Yermakov.',
    author='Klaus Wong',
    install_requires=[],
)