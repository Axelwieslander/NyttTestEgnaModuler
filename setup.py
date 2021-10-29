import setuptools

long_description = "na"

setuptools.setup(
    name='GoodToHave',
    version='0.0.1',
    author='Axel WJ',
    author_email='Axel Wieslander Jansson',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Axelwieslander/GoodToHave',
    project_urls={
        "Bug Tracker": "https://github.com/Axelwieslander/GoodToHave/issues"
    },
    license='MIT',
    packages=['GoodToHave'],
    install_requires=['requests']
)
