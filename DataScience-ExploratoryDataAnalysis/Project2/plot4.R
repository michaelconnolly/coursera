library(ggplot2)
library(sqldf)

## Load our data!
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

## Fix column names so later transformations work.
names(SCC)[4] <- "EISector"

## add the activities labels and merge up the training data.
merged_table2 <- sqldf("SELECT NEI.*, SCC.EISector FROM NEI LEFT JOIN SCC ON NEI.SCC=SCC.SCC")
merged_table3 <- sqldf("SELECT * FROM merged_table2 WHERE EISector LIKE '%Coal%' ")


##training_label_descrip$id = seq(1, nrow(training_label_descrip))
##training_data$id = seq(1, nrow(training_labels))
##training_subject$id = seq(1, nrow(training_subject))
##training_all <- sqldf("SELECT training_subject.subject_id, training_label_descrip.activity_name, training_data.* FROM training_subject, training_label_descrip, training_data WHERE training_subject.id = training_label_descrip.id AND training_subject.id = training_data.id")


##justonezip <- NEI[NEI$fips=="24510",]
plot4data <- aggregate(merged_table3$Emissions, by = list(year = merged_table3$year), FUN = "sum")
png(file="plot4.png")
#qplot(year, x, data=plot4data)
barplot(plot4data$x, names.arg=plot4data$year)
dev.off() 