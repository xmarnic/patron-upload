from setuptools import setup, find_packages

setup(
    name="flatten-users",
    version="0.1.0",
    author="Nicholas Marlin",
    author_email="mail@nickmarl.in",
    description="Produce a SirsiDynix Symphony LDUSER flat file",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "et-xmlfile==1.1.0",
        "iniconfig==2.0.0",
        "numpy==1.26.4",
        "openpyxl==3.1.3",
        "packaging==24.1",
        "pandas==2.2.2",
        "pluggy==1.5.0",
        "pytest==8.2.2",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.1",
        "six==1.16.0",
        "tzdata==2024.1",
    ],
    entry_points={
        "console_scripts": [
            "flatten-users=flatten_users:main",
        ],
    },
    python_requires=">=3.7",
)
