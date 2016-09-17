from distutils.core import setup
setup(
  name = 'heavymouse',
  packages = ['heavymouse'], # this must be the same as the name above
  version = '1.1',
  description = 'Give your mouse some mass',
  author = 'Alex PB',
  author_email = 'chozabu@gmail.com',
  url = 'https://github.com/chozabu/HeavyMouse', # use the URL to the github repo
  download_url = 'https://github.com/chozabu/HeavyMouse/tarball/1.1', # I'll explain this in a second
  keywords = ['joke', 'fun', 'physics'], # arbitrary keywords
  install_requires=['python-xlib', 'PyUserInput', 'defopt'],
  classifiers = [],
)
