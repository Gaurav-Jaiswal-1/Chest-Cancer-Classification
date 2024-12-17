import setuptools

with open("README.md", "r", encoding="utf-8") as f:
  long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "Chest-Cancer-Classification"
AUTHOR_NAME = "Gaurav Jaiswal"
SRC_REPO = "ChestCancerClassification"
AUTHOR_EMAIL = "jaiswalgaurav863@gmail.com"


setuptools.setup(
  name = SRC_REPO,
  version = __version__,
  author=AUTHOR_NAME,
  author_email=AUTHOR_EMAIL,
  description="A small python package for CNN app",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/Gaurav-Jaiswal-1/Chest-Cancer-Classification",
  project_urls = {
    "Bug tracker" : "https://github.com/Gaurav-Jaiswal-1/Chest-Cancer-Classification/issues",
  },
  package_dir= {"" : "src"},
  packages= setuptools.find_packages(where="src")

  
)


