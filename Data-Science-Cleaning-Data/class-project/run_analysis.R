
## Required libraries/packages.
library(sqldf)

## Load the features labels.
features_labels_raw <- read.table("dataset\\features.txt")
features_labels <- features_labels_raw[2]
features_labels <- t(features_labels)
##features_labels_raw$colid <- seq(3, (nrow(features_labels_raw) + 2))
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

## only take the columns we want
##both_all_paired_down <- both_all[,features_labels_wewant$colid]



