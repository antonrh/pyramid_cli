import os

from setuptools import setup, find_packages

root_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root_path, 'README.md')) as f:
    README = f.read()
with open(os.path.join(root_path, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.7',
    'click==6.6'
]

setup(
    name='pyramid_cli',
    version='0.1',
    description='Pyramid Click integration',
    long_description=README + '\n\n' + CHANGES,
    author='Anton Ruhlov',
    author_email='antonruhlov@gmail.com',
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires + [
        'pytest==2.9.1',
    ],
)
