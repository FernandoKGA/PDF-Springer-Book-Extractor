# PDF-Springer-Book-Extractor
A Selenium/Python extractor of the free Springer books available

## Programs needed

* Python 3.8.2
* PyPDF2 package
* requests package
* Selenium WebDriver
* Geckodriver

## Instructions

First, download the webdriver associated with the browser you use. Follow the instructions to download it and make available in the PATH. (By now, it's locked at Firefox)

Secondly, using `pip3` the following packages: `PyPDF2`, `requests` and `selenium`. Shortcut for it: `pip3 install PyPDF2 && pip3 install requests && pip3 install selenium` (if you're using Unix like).

Thirdly, create a folder called `books` in the repository folder, in order to receive the books.

Then, run: `python3 link-extractor.py && python3 download-books.py`. The first script will get the links from the PDF, and the next will download the books one by one. 