
#
# E-shopping-scraper

Python attacking E-commerce sites :)

execute the crawler in this way:

scrapy crawl flip\_spider

## **Description:**

This is a python based project which is used to scrape the online shopping sites search results page. It chooses the first product to appear on the search result of the product user inputs from 5 different websites and exports it to the csv file and opens it automatically.Once you started gathering the data, you could do run many analysis like price range variation, offers, stock status, Link for the product, Ratings…

in screens directory I have uploaded our first version screenshots. you can take a look and give us the feedback.

## **Tools:**

- python
- Xpath
- scrapy

## **How to execute this project?**

**STEP-1**

Please install scrapy using the below commands

pip install scrapy

if you are using anaconda use the below

conda install -c conda-forge scrapy

conda install -c conda-forge/label/cf201901 scrapy

**STEP-2**

Navigate cmd to your desired folder run commands

scrapy startproject flip

scrapy genspider flip\_spider

**STEP-3**

paste all the files in the github folder to the above created project location and run

**STEP-4**

navigate to the settings.py file and specify the path where your csv file has to be saved (please don&#39;t replace the &#39;r&#39;)
 ![alt text](https://github.com/vishnu-sagar/data-science/blob/master/scraping%20e-commerce%20sites/screens/file.PNG)
 ![]
That&#39;s it you are ready !!!!!

**LAST STEP**(**don&#39;t get tired)

To start crawling run

scrapy crawl flip\_spider

you will be prompted to enter the desired product name
![alt text](https://github.com/vishnu-sagar/data-science/blob/master/scraping%20e-commerce%20sites/screens/input.PNG)

SMASH that ENTER key!!!!!!!!!!.

Results will be saved and automatically opened in a csv file.

Note: Please close the csv file before searching the same product again (we cant write data if a file is being locked by another application)

## **Features:**

- Crawling all the sites in a single spider
- Case-insensitive search
- Stock status
- No worries for No results.

I am  working for further releases for the extensive use of customers.

## **Screenshots:**

###Demo outplut:
![alt text](https://github.com/vishnu-sagar/data-science/blob/master/scraping%20e-commerce%20sites/screens/output.PNG)
Thanks for your time.

Please take a look at the videos in demo videos folder :)

