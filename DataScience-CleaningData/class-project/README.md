---
title: "README.md"
author: "mc"
date: "Saturday, October 25, 2014"
output: html_document
---

The R code script "run_analysis.R" implements the course project for "Getting and Cleaning Data", aka getdata-008, on coursera.com.

The starting data set is here: https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip

The data is unzipped and in the "dataset" folder.

When running the script, set your working directory to the same folder, so it can find the "dataset" folder.

The script does the following, per the specification outlined in the assignment:

* Import all the "training" data and build one flat table, but including only the mean and standard deviation variables.
* Import all the "test" data and build one flat table, but including only the mean and standard deviation variables.
* Merge the "training" and "test" data together.
* Create a summary table that averages each variable for each subject activity.
* Exports the summary table into a file called "tidydata.txt" into the working directory.

Note that this script requires the "sqldf" package to be installed.

A more in depth description of the data can be found in CodeBook.md.



