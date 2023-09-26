from setuptools import setup, find_packages

setup(
    name='dataframe_comparer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ]
)