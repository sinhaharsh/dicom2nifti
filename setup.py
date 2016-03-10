from distutils.core import setup
from setuptools import find_packages

long_description = """
With this package you can convert dicom images to nifti files.
There is support for most anatomical CT and MR data.
For MR specifically there is support for most 4D data (like DTI and fMRI)
"""
setup(
    name='dicom2nifti',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    version='0.0.1.dev2',
    description='package for converting dicom files to nifti',
    long_description=long_description,
    author='icometrix',
    author_email='it@icometrix.com',
    url='https://github.com/icometrix/dicom2nifti',
    download_url='https://github.com/icometrix/dicom2nifti/tarball/0.0.1.dev2',
    keywords=['dicom', 'nifti', 'medical imaging'],
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux'],
    install_requires=['nibabel', 'pydicom', 'numpy', 'six']

)
