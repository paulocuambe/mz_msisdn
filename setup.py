import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mznumber",  # Replace with your own username
    version="0.0.1",
    author="Paulo Amosse Cuambe",
    author_email="pamossecuambe@gmail.com",
    description="A small package to validate if a mozambican number is formated properly.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulocuambe/mznumber",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
