from Cython.Build import cythonize
from setuptools import setup
import re


with open('README.md') as f:
    long_description = f.read()


with open('truncjson/version.py', 'r', encoding='utf-8') as f:
    version = '0.0.0'
    re_groups = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE)
    if re_groups:
        version = re_groups.group(1)


setup(
    name='truncjson',
    version=version,
    description='Truncated JSON completer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Misam saki',
    author_email='justmisam@gmail.com',
    url='https://github.com/justmisam/truncjson',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers'
    ],
    packages=['truncjson'],
    ext_modules=cythonize('truncjson/*.pyx'),
    zip_safe=False
)
