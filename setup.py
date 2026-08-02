import pathlib

from setuptools import setup, find_namespace_packages

HERE = pathlib.Path(__file__).parent

# The PyPI project page renders this. 
LONG_DESCRIPTION = (HERE / "README.rst").read_text(encoding="utf-8")

setup(
    name="infi.dtypes.wwn",
    version="0.2.0",
    author="Infinidat",
    author_email="info@infinidat.com",
    url="https://github.com/Infinidat/infi.dtypes.wwn",
    # SPDX identifier for the Python Software Foundation License 2.0. setuptools
    # 77+ emits this as the Metadata 2.4 License-Expression field; older
    # versions fall back to the legacy License field, so this stays buildable
    # with the setuptools>=64 declared in pyproject.toml.
    license="PSF-2.0",
    description="Datatype for FiberChannel World Wide Name",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",

    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    # `infi` and `infi.dtypes` are PEP 420 implicit namespace packages, which
    # arrived in Python 3.3. 
    python_requires=">=3.3",

    package_dir={"": "src"},
    # find_namespace_packages, not find_packages: the namespace directories
    # have no __init__.py, so find_packages would return an empty list and the
    # built distribution would silently contain no modules at all.
    packages=find_namespace_packages("src"),
    include_package_data=True,
    zip_safe=False,
)
