from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Math quiz package'
LONG_DESCRIPTION = 'A Python package to test your knowledge with elementary mathematical calculations.'

setup(
    name="math_quiz", 
    version=VERSION,
    author="Sambhav Sahani",
    author_email="ssambhav3672@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["math", "quiz"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
