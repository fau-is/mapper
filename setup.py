import pip
try:
    from setuptools import setup, find_packages
    import_success = True
except ImportError:
    from distutils.core import setup
    import_success = False


def install(packages):
    for package in packages:
        pip.main(['install', package])


if import_success:
    setup(
        name='label_mapper',
        version='0.1.0',
        author='Sebastian Dunzer',
        author_email='sebastian.dunzer@fau.de',
        packages=find_packages(),
        license='LICENSE.txt',
        description='Maps event labels to activity labels',
        long_description=open('README.md').read(),
        install_requires=[
            'pm4py'
        ]
    )

else:
    setup(
        name='label_mapper',
        version='0.1.0',
        author='Sebastian Dunzer',
        author_email='sebastian.dunzer@fau.de',
        packages=['label_mapper'],
        license='LICENSE.txt',
        description='Logger for RPA related information',
        long_description=open('README.md').read()
    )

    with open("requirements.txt", "r") as f:
        install(f.read().splitlines())
