# AUDIOWORD 

PDF to audiobook converter using [Python](https://www.python.org/), [PyPDF](https://pypdf2.readthedocs.io/en/latest/) and [Google cloud Text-to-speech](https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3/#0).

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info

This is a command line program that converts PDF files to an audiobook (PDF files under 5000 characters).  

## Technologies
Project is created with:
* Python version: 3.10.6
* PyPDF2 version: 2.12.1
* Google cloud Text-to-speech version: 2.13.0
	
## Setup

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer.\
From your command line run:

```
# Clone this repository
$ git clone https://github.com/lasanthamudalige/convert-pdf-to-audiobook.git

# Go into the repository
$ cd convert-pdf-to-audiobook/

# To install all dependencies
$ pip install -r requirements.txt
```


## Usage

To run this project in Linux/Unix:

```
$ python3 main.py pdf_file_name
```

To run this project in Windows:

```
$ python main.py pdf_file_name
```

## License 
This project is open source and available under the [MIT License](https://github.com/lasanthamudalige/convert-pdf-to-audiobook/blob/main/LICENSE).
