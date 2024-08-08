from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mexico_einvoice/__init__.py
from mexico_einvoice import __version__ as version

setup(
	name="erpnext_mexico_cfdi",
	version=version,
	description="Mexico CFDI",
	author="Nobody",
	author_email="contacto@pcmloscabos.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
