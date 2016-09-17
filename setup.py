from distutils.core import setup
setup(
  name = 'heavymouse',
  packages = ['heavymouse'], # this must be the same as the name above
  version = '0.7',
  description = 'Give your mouse some mass',
  author = 'Alex PB',
  author_email = 'chozabu@gmail.com',
  url = 'https://github.com/chozabu/HeavyMouse', # use the URL to the github repo
  download_url = 'https://github.com/chozabu/HeavyMouse/tarball/0.7', # I'll explain this in a second
  keywords = ['joke', 'fun', 'physics'], # arbitrary keywords
  install_requires=['python-xlib',],
  scripts=[ '/heavymouse/heavymouse' ],
  classifiers = [],
)
