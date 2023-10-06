all:
    # install pycocotools locally
	`(which python3 || which python)` setup.py build_ext --inplace
	rm -rf build

install:
	# install pycocotools to the Python site-packages
	`(which python3 || which python)` -m pip install --use-feature=in-tree-build .
	rm -rf build