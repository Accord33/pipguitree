from setuptools import setup, find_packages

setup(
    name='pipguitree',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pipdeptree'
    ],
    entry_points={
        'console_scripts': [
            'pipguitree = pipguitree.app:main',
        ],
    },
)
