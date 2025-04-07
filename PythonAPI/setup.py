# setup.py (minimal shim for dynamic configuration)
from setuptools import setup
import numpy as np

def build_with_numpy():
    from setuptools import Extension
    ext_modules = [
        Extension(
            'pycocotools._mask',
            sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
            include_dirs=[np.get_include(), '../common'],
            extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
        )
    ]
    return {"ext_modules": ext_modules}

setup(**build_with_numpy())
