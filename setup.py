import sys
import webbrowser
from distutils.core import setup

trailer_url = 'http://pytorch.org/#pip-install-pytorch'
message = 'You should install pytorch from http://pytorch.org'

argv = lambda x: x in sys.argv

if (argv('install') or  # pip install ..
        (argv('--dist-dir') and argv('bdist_egg')) or  # easy_install
        argv('bdist_wheel')):  # modern pip install
    webbrowser.open_new(trailer_url)
    raise Exception(message)


setup(
    name='pytorch',
    version='0.1.11b1',
    maintainer='Thomas Grainger',
    maintainer_email='pytorch@graingert.co.uk',
    long_description=message,
    url=trailer_url,
)
