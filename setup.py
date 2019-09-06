from distutils.core import setup
setup(
  name = 'telepy',         # How you named your package folder (MyLib)
  packages = ['telepy'],   # Chose the same as "name"
  version = 'v0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python Class to convert numbers to English Words, English Words to phone numbers. Currently support 10-11 phone numbers',   # Give a short description about your library
  author = 'Zipei Wei',                   # Type in your name
  author_email = 'zipeiwei123@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/zipeiwei123/Telephone_Book',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/zipeiwei123/Telephone_Book/archive/v0.4.tar.gz',    # I explain this later on
  keywords = ['Phoneword', 'Python', 'number_to_words'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          're',
          'enchant',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license,   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)
