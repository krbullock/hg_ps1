from setuptools import setup
 
setup(
    name='hg_ps1',
    version='0.0.1',
    author='Kevin Bullock',
    url='http://bitbucket.org/krbullock/hg_ps1/',
    py_modules=['hg_ps1'],
    entry_points={
        'console_scripts': [
            '__hg_ps1 = hg_ps1:main',
        ],
    },
)
