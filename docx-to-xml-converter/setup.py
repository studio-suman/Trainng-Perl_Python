from setuptools import setup, find_packages

setup(
    name='docx-to-xml-converter',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A converter that transforms DOCX files to XML while retaining UI elements like styling, color, tables, and content.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'python-docx',
        'lxml',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)