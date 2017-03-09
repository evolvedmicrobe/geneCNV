from setuptools import setup, find_packages
import os
from cnv import __version__

VERSION = __version__


# Hack to avoid specifying requirements in two places, see:
# http://stackoverflow.com/questions/14399534/how-can-i-reference-requirements-txt-for-the-install-requires-kwarg-in-setuptool
requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
with open(requirements_file) as f:
    all_reqs = f.read().splitlines()

required = [x for x in all_reqs if not x.startswith("git+")]
# Specially handle Git repos
# https://mike.zwobble.org/2013/05/adding-git-or-hg-or-svn-dependencies-in-setup-py/
gits = [x for x in all_reqs if x.startswith("git+")]
deps = []
for repo in gits:
    rep_name = repo.split("/")[-1].replace(".git", "")
    required.append(rep_name)
    deps.append(repo + "#egg=" + rep_name)


setup(name='cnv',
      version=VERSION,
      url='https://github.com/genepeeks/dmd',
      description='Library and command line scripts to find copy number variation.',
      packages=find_packages(),
      install_requires=required,
      dependency_links=deps,
      entry_points={
          'console_scripts': 'cnv=cnv.evaluate_sample:main'
      },
      zip_safe=False)
