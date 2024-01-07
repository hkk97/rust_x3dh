from setuptools import find_packages, setup

setup(
    name='rustx3dh',
    packages=find_packages(include=['rustx3dh']),
    version='0.0.1',
    description='Embeded the xxxdh, which iplementation of the Extended Triple Diffie-Hellman key exchange protocol written in Rust, on Python. xxxdh is written by Olexander Yermakov.',
    author='Klaus Wong',
    install_requires=[],
)