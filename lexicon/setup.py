try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
try:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
except:
    print('No README found')

config = {
    'description': 'My Project Name',
    'author': 'J. Michael Thurman',
    'url':'project_url',
    'download_url':'where to download project',
    'author_email':'jmthurman@cloudbrook.net',
    'version':'0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectName'
}

setup(**config)

# From setuptools documentation:
# import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name="example_pkg",
#     version="0.0.1",
#     author="Example Author",
#     author_email="author@example.com",
#     description="A small example package",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/pypa/sampleproject",
#     packages=setuptools.find_packages(),
#     classifiers=(
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ),
# )
