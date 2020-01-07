import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'mvl',
    version = '0.2.0',
    author = 'Andrew J. Young',
    author_email = 'andrewjunyoung1@gmail.com',
    description = 'A package which implements various systems of n valued ' \
        'logic.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/andrewjunyoung/mvl',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: Public Domain',
    ],
    python_requires = '>=3.6',
)
