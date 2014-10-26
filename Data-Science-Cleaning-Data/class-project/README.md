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

## Required libraries/packages.
library(sqldf)

## Load the features labels.
features_labels_raw <- read.table("dataset\\features.txt")
features_labels <- features_labels_raw[2]
features_labels <- t(features_labels)
features_labels_wewant <- sqldf("select V1 from features_labels_raw where V2 LIKE '%mean()%' OR V2 LIKE '%std()'")

## Read in training data.
training_data <- read.table("dataset\\train\\X_train.txt", colClasses = "numeric", col.names=features_labels)
training_data <- training_data[,features_labels_wewant$V1]
training_labels <- read.table("dataset\\train\\y_train.txt", colClasses=c("numeric"), col.names=c("activity_id"))
training_subject <- read.table("dataset\\train\\subject_train.txt", colClasses=c("numeric"), col.names=c("subject_id"))

## Read in test data.
test_data <- read.table("dataset\\test\\X_test.txt", colClasses = "numeric", col.names=features_labels)
test_data <- test_data[,features_labels_wewant$V1]
test_labels <- read.table("dataset\\test\\y_test.txt", colClasses=c("numeric"), col.names=c("activity_id"))
test_subject <- read.table("dataset\\test\\subject_test.txt", colClasses=c("numeric"), col.names=c("subject_id"))

## Load the activities labels.
activity_labels <- read.table("dataset\\activity_labels.txt", colClasses=c("numeric", "character"), col.names=c("activity_id", "activity_name"))

## add the activities labels and merge up the training data.
training_label_descrip <- sqldf("SELECT training_labels.activity_id, activity_name FROM training_labels LEFT JOIN activity_labels USING(activity_id)")
training_label_descrip$id = seq(1, nrow(training_label_descrip))
training_data$id = seq(1, nrow(training_labels))
training_subject$id = seq(1, nrow(training_subject))
training_all <- sqldf("SELECT training_subject.subject_id, training_label_descrip.activity_name, training_data.* FROM training_subject, training_label_descrip, training_data WHERE training_subject.id = training_label_descrip.id AND training_subject.id = training_data.id")

## add the activities labels and merge up the test data.
test_label_descrip <- sqldf("SELECT test_labels.activity_id, activity_name FROM test_labels LEFT JOIN activity_labels USING(activity_id)")
test_label_descrip$id = seq(1, nrow(test_label_descrip))
test_data$id = seq(1, nrow(test_labels))
test_subject$id = seq(1, nrow(test_subject))
test_all <- sqldf("SELECT test_subject.subject_id, test_label_descrip.activity_name, test_data.* FROM test_subject, test_label_descrip, test_data WHERE test_subject.id = test_label_descrip.id AND test_subject.id = test_data.id")

## Merge the training and test datasets.
both_all <- rbind(training_all, test_all) 
both_all$id = NULL

## Create a summary table that averages each variable for each subject/activity.
both_summary <- aggregate(both_all, FUN=mean, by=list(subject = both_all$subject_id, activity = both_all$activity_name))
both_summary$subject_id = NULL
both_summary$activity_name = NULL

## Output the new combined table
write.table(both_summary, file="tidydataset.txt", row.names=FALSE, append=FALSE)

