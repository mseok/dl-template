from setuptools import find_packages, setup

setup(
    name= , # NOTE: ADD NAME
    version="0.1.0",
    packages=find_packages(where="src"),  # Tell setuptools to find packages under 'src'
    package_dir={"": "src"},  # Tell setuptools that package root is 'src'
    install_requires=[
        # List your project's dependencies here.
        # E.g., 'numpy', 'pandas', etc.
    ],
    python_requires=">=3.9",  # Minimum version requirement of the package
    author="Seokhyun Moon",
    author_email="mshmjp@kaist.ac.kr",
    description= , # NOTE: ADD DESCRIPTION
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # if your README is markdown
    url= , # NOTE: ADD URL
)
