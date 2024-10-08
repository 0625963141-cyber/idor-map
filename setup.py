from setuptools import setup, find_packages

setup(
    name='idor-map',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        # Ajoutez toutes les dépendances nécessaires ici
    ],
    entry_points={
        'console_scripts': [
            'idor-map=idor_map.cli:main',
        ],
    },
    description='Tool for detecting Insecure Direct Object References (IDOR) in web applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='cs778',
    author_email='cs7778@github.com',
    url='https://github.com/0625963141-cyber/idor-map',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        # Ajoutez d'autres classifications appropriées
    ],
)
