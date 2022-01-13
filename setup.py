import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="symbol_convert",
    version="0.1.12",
    author="symbol_convert",
    author_email="fangling@outlook.com",
    description="替换掉字符串中的中文符号以及全角符号转换为半角符号",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Caaby/symbol_convert",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
