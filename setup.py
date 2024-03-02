import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rust_x3dh",
    version="0.1.1",
    author="Klaus Wong",
    author_email="wch.klaus@gmail.com",
    description="Embeded the xxxdh, which implementation of the Extended Triple Diffie-Hellman key exchange protocol written in Rust, on Python. xxxdh is written by Olexander Yermakov.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hkk97/rust_x3dh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Rust",
    ],
    python_requires=">=3.9",
)