import re
import codecs

from setuptools import setup
import upsidedown

VERSION = str(upsidedown.__version__)
(AUTHOR, EMAIL) = re.match('^(.*?)\s*<(.*)>$', upsidedown.__author__).groups()
URL = upsidedown.__url__
LICENSE = upsidedown.__license__


with codecs.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

setup(name='ckuehl-upsidedown',
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description='Fork that supports Python 3',
    long_description=long_description,
    url=URL,
    download_url='http://github.com/cburgmer/upsidedown/downloads',
    py_modules=['upsidedown'],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'upsidedown = upsidedown:main',
        ],
    },
    license=LICENSE,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Topic :: Text Processing',
        ])
