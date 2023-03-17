from setuptools import find_packages, setup
from telco_churn import __version__

LOCAL_REQUIREMENTS = [
    "pyspark==3.2.1",
    "delta-spark==1.1.0",
    "scikit-learn",
    "pandas",
    "mlflow",
]

TEST_REQUIREMENTS = [
    # development & testing tools
    "pytest",
    "coverage[toml]",
    "pytest-cov",
    "dbx>=0.7,<0.8"
]

setup(
    name='telco_churn',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel', 'setuptools',],
    install_requires=['python-dotenv'],
    extras_require={"local": LOCAL_REQUIREMENTS, "test": TEST_REQUIREMENTS}, 
    version=__version__,
    description='Demo repository implementing an end-to-end MLOps workflow on Databricks. Project derived from dbx '
                'basic python template',
    authors='Joseph Bradley, Rafi Kurlansik, Matthew Thomson, Niall Turbitt'
)