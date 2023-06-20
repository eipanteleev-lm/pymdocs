from setuptools import setup, find_packages

setup(
    name='pymdocs',
    description='Library generating markdown code reference',
    version='1.0.0',
    packages=find_packages(),  # list of all packages
    python_requires='>=3.7',  # any python greater than 3.7
    include_package_data=True,
    author='Evgenii Panteleev',
    keyword='',
    long_description='''
        Simple package to generate Code Reference from source in Markdown
    ''',
    long_description_content_type="text/markdown",
    dependency_links=[],
    author_email='',
    classifiers=[]
)
