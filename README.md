# UF Lawsuits Machine Learning

This is a text-classification machine learning program that aims to categorize lawsuits involving the University of Florida by topic. We used complaints only filed electronically with the Alachua County Clerk of Court via its [website](alachuaclerk.org/court_records/gis/index.cfm?section=results). We wound up downloading these by hand for the project, though we later got a scraper to retrieve these documents working after learning Firefox defaults to a PDF viewer. We initially chose to tailor our data to cases from 2012 to 2017 for the sake of time.

Both the scraper and the test.py script that creates the model with which to predict the classification have limitations, which we will discuss further below. Full disclosure: the accuracy for the script tends to range from 40 to 50 percent. This was a project done to understand and practice the concept of machine learning by University of Florida seniors [Caitlin Ostroff](https://twitter.com/ceostroff) and [Gabrielle Calise](https://twitter.com/gabriellecalise). The more data we added, the higher the accuracy went, so in the future we'd like to expand the data within it in the hopes of improving that score and confidence in case classification.

## Instructions
First, let's install some things. You should be able to get away with just the pip install for requirements, but Anaconda also packages a lot of the libraries you need for machine learning together. That's a direct download that you can find [here](https://www.anaconda.com/download/).
```
pip install -r requirements.txt
```
To run the machine learning script, just run the test script.
```
python test.py
```
This will link to the pre-made cases.csv and predictions.csv. Cases refers to complaints filed in the Alachua Clerk of Court involving the University of Florida. Predictions.csv contains two cases that after the script runs a model, will try to predict what classification (among those existing in current cases) will be used to predict the category of the complaint, using the text in the csv. Some categories include medical malpractice, public records, debt collection and patents, among others. We have two text files loaded into  predictions.csv that we are using to make predictions from.

When you run the script, it will print the accuracy score and the predictive labels for the lawsuits in the predictions csv.

It may also pop a message saying the software has depreciated. It's something we plan to upgrade in the future.

## How We Did It
The pdfs from the Clerk of Court were not already processed using OCR, so we used CometDocs to parse them and output text files. CometDocs is free for IRE members and you can sign up [here](https://www.ire.org/blog/ire-news/2013/05/22/ire-announces-partnership-cometdocs/).

After getting the text, we made the csv of all the cases, using only the initial complaints filed in court, and read through them ourselves to classify them. Because we did supervised machine learning, we needed to teach the script what label matched what text so we could train it to see what words were commonly associated with the label. In our script, the scikitlearn library MultinomialNB does this by assigning numerical weights to the words.  

We found this [walkthrough](https://nlpforhackers.io/text-classification/) on text classification, which formed the basis for our script. We also used these [videos](https://www.youtube.com/watch?v=cKxRvEZd3Mw&list=PLT6elRN3Aer7ncFlaCz8Zz-4B5cnsrOMt) by Google Developers to help us understand text-classification machine learning and walk use through writing predictions after we trained the model.

## Limitations and Future Goals
For the sake of transparency, all of our text files are in the data folder (this is not necessary to run the script). Files that were heavily redacted or contained sensitive information (such as sexual violence), were not used and therefore are not posted. For files exceeding 50,000 characters, we imported as much as we could. We also only used complaints because that's usually the starting point in a case. We ignored cases without complaints and only coversheets due to the lack of information they usually contained. We created the scraper to get all documents as a remedy to this for the future.

Our scraper, which can be run with the following code, will download all files in court cases from Jan. 1, 2012 to Dec. 31, 2017. Currently, the script downloads them as .cfm files but honest to God if you just change the file extension in Finder to .pdf, it's fine. This is something we hope to fix in the future.

Other limitation of the scraper was the captcha. In order to bypass it with code (you enter it once after Firefox pops the website), we would have had to download the image and analyze the letter and input those, and it would up being easier for just one clerk of court to put it in manually. This is why the script pauses for 10 seconds. In the future, we plan to implement a more robust process, especially as it would be useful to analyze court cases of many schools in many counties.

Use this code to run the scraper.

```
python uf_lawsuits_scraper.py
```

We would also like to replace the Cometdoc OCR with a Python library in the future to generate the text files to automatically write into the csv.
