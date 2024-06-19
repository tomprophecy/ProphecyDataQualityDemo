from setuptools import setup, find_packages
packages_to_include = find_packages(exclude = ['test.*', 'test', 'test_manual'])
setup(
    name = 'maciejdemos_dataquality',
    version = '1.3',
    packages = packages_to_include,
    description = '',
    install_requires = [
'pydeequ', ],
    data_files = ["resources/extensions.idx"]
)
