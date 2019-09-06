from distutils.core import setup

with open("README.md", "r") as fh:
    l_description = fh.read()

setup(
  name = 'phonewordzp',         
  packages = ['phonewordzp'],   
  version = 'v0.6',      
  license='MIT',        
  description = 'A Python Class to convert numbers to English Words, English Words to phone numbers. Currently support 10-11 phone numbers',   # Give a short description about your library
  author = 'Zipei Wei',                   
  author_email = 'zipeiwei123@gmail.com',      
  url = 'https://github.com/zipeiwei123/Telephone_Book',
  long_description=l_description,
  long_description_content_type="text/markdown",   
  download_url = 'https://github.com/zipeiwei123/Telephone_Book/archive/v0.6.tar.gz',    
  keywords = ['Phoneword', 'Python', 'number_to_words'],   
  
  classifiers=[
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
  include_package_data=True)
