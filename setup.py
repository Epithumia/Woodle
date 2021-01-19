from setuptools import setup

requires = [
    'pandas',
    'xlrd==1.2.0',
]

setup(
    name="Woodle",
    version="0.1",
    description="Outil pour trnsformer un fichier de notes Moodle en fichier SNW.",
    url="https://git.iut-orsay.fr/rafael.lopez/woodle",
    packages=['woodle'],
    install_requires=requires,
    entry_points={
        'console_scripts': ['woodle=woodle.woodle:main'],
    }
)
