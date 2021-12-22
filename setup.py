"""Setup for the intimations package."""

#from distutils.core import setup
from setuptools import setup,find_packages

with open('README.md','r') as f:
    README = f.read()

setup(
    author="ABHIJITH BOPPE",
    author_email="abhijithas.eh@gmail.com",
    name='intimations',
    license="MIT",
    description='''
    Description: push notifications with different icons, beep sound with different types of sound, telegram message intimation (requires your botAPI and ChatID), command line''',
    version='v1.0',
    long_description_content_type='text/markdown',
    long_description=README,
    keywords=['intimation', 'intimations', 'desktop notifications', 'windows notifications', 'cloud notification', 'command line notifications', 'process notifications', 'process intimation' 
    'intimate after done', 'cross platform notifications', 'buzzer sound notifications', 'message from cloud', 'cloud to mobile', 'mobile notification after a process is done',
    'system to mobile', 'laptop to mobile', 'cloud process intimation', 'sound intimations', 'buzzer intimations', 'intimate about process'],
    url='https://github.com/AbhijithAJ/intimations',
    download_url='https://github.com/AbhijithAJ/intimations/archive/refs/tags/v1.0.tar.gz',
    packages=find_packages('intimations'),
    python_requires=">=3.2",
    install_requires=['playsound==1.2.2', 'win10toast ; platform_system=="Windows"'],
    include_package_data=True,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Communications',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
    ],
)