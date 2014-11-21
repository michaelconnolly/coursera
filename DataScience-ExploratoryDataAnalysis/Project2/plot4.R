library(ggplot2)
library(sqldf)

## Load our data!
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

## Fix column names so later transformations work.
names(SCC)[4] <- "EISector"

## add the activities labels and merge up the training data.
merged_table4 <- sqldf("SELECT NEI.*, SCC.EISector FROM NEI LEFT JOIN SCC ON NEI.SCC=SCC.SCC")
merged_table4 <- sqldf("SELECT * FROM merged_table4 WHERE EISector LIKE '%Coal%' ")

## Question: Across the United States, how have emissions from coal combustion-related sources changed from 1999-2008?

##justonezip <- NEI[NEI$fips=="24510",]
plot4data <- aggregate(merged_table4$Emissions, by = list(year = merged_table4$year), FUN = "sum")
png(file="plot4.png")
opt <- options("scipen" = 20)
barplot(plot4data$x, names.arg=plot4data$year, main="Coal combusion-related Emissions in USA")
options(opt)
dev.off() 