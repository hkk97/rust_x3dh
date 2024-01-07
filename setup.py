from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Intended Audience :: Developers",

    "License :: OSI Approved :: MIT License",

    "Programming Language :: Rust",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"
]

setup(
    name='rustx3dh',
    version='0.0.1',
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['rustx3dh']),
    description='Embeded the xxxdh, which iplementation of the Extended Triple Diffie-Hellman key exchange protocol written in Rust, on Python. xxxdh is written by Olexander Yermakov.',
    author='Klaus Wong',
    install_requires=[],
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    classifiers=classifiers,
)
