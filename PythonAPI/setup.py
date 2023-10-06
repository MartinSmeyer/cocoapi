import platform
from pathlib import Path
from setuptools import setup, Extension

import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
        Extension(
            'pycocotools._mask',
            sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
            include_dirs = [np.get_include(), '../common'],
            extra_compile_args=[] if platform.system()=='Windows' else
            ['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
        )
    ]

try:
    readme = Path(__file__).parent.parent.joinpath("README.md").read_text("utf-8")
except FileNotFoundError:
    readme = ""


setup(
    name='pycocotools',
    description='Official COCO APIs for the BOP datasets',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/MartinSmeyer/cocoapi",
    packages=['pycocotools'],
    package_dir={'pycocotools': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3'
    ],
    version='2.0.7.post1',
    ext_modules=ext_modules
)
