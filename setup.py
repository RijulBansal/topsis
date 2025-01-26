from setuptools import setup, find_packages

setup(
    name='Topsis-<FirstName>-<RollNumber>',  # Replace <FirstName> and <RollNumber>
    version='1.0.0',
    author='<Your Name>',
    author_email='<Your Email>',
    description='A Python package for implementing the TOPSIS decision-making method',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.0',
        'numpy>=1.19.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
