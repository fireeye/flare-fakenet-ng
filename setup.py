import os
import platform

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    "pydivert==1.0.2",
    "dpkt",
    "dnslib",
    "netifaces",
    "pyftpdlib",
    "pyopenssl",
]

if platform.system() == 'Windows':
    requirements.append("pydivert")
elif platform.system().lower().startswith('linux'):
    requirements.append("netfilterqueue")

setup(
    name='FakeNet NG',
    version='2.0',
    description="",
    long_description="",
    author="Peter Kacherginsky",
    author_email='peter.kacherginsky@fireeye.com',
    url='https://www.github.com/fireeye/flare-fakenet-ng',
    packages=[
        'fakenet',
    ],
    package_dir={'fakenet': 'fakenet'},
    package_data={'fakenet': ['*.pem','diverters/*.py', 'listeners/*.py', 'configs/*.ini', 'defaultFiles/*', 'lib/64/*', 'lib/32/*']},
    entry_points={
        "console_scripts": [
            "fakenet=fakenet.fakenet:main",
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='fakenet-ng',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
    ],
)
