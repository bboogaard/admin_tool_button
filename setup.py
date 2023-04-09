from setuptools import setup, find_packages
from admin_tool_button.version import Version


setup(name='admin_tool_button',
     version=Version('1.0.0').number,
     description='Extra tool buttons for Django admin',
     long_description=open('README.md').read().strip(),
     author='Bram Boogaard',
     author_email='padawan@hetnet.nl',
     url='https://github.com/bboogaard/admin_tool_button',
     packages=find_packages(include=['admin_tool_button', 'admin_tool_button.contrib']),
     install_requires=[
         'pytest',
         'pytest-cov',
         'pytest-django==4.5.2',
         'django==3.2'
     ],
     license='MIT License',
     zip_safe=False,
     keywords='Auth0 SSO',
     classifiers=['Packages', 'Auth0 SSO'])
