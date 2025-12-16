import setuptools

with open ("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    

_version_ = '0.0.0'
REPO_NAME = 'Text-Summarizer'
AUTHOR_USER_NAME = 'Subamprasad'
SRC_REPO = 'https://github.com/Subamprasad/Text-Summarizer.git'
AUTHOR_EMAIL = 'subamprasad4311@gmail.com'



setuptools.setup(
    name=REPO_NAME,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Text Summarizer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=SRC_REPO,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.6',
    install_requires=[],
)

