# AUDIOWORD 

Audiobook converter using [Python](https://www.python.org/), [PyPDF2](https://pypdf2.readthedocs.io/en/latest/) and [gTTS](https://github.com/pndurette/gTTS).

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Usage](#usage)

## General info

This is a command line program converts PDF files to an audiobook using google Text-to-speech api.  

## Technologies
Project is created with:
* Python version: 3.10.6
* PyPDF2 version: 2.12.1
* gTTs version: 2.3.0
	
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
