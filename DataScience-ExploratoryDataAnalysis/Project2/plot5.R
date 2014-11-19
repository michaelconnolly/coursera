library(ggplot2)
library(sqldf)

## Load our data!
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

## Fix column names so later transformations work.
names(SCC)[3] <- "ShortName"
names(SCC)[4] <- "EISector"

## add the activities labels and merge up the training data.
merged_table <- sqldf("SELECT NEI.*, SCC.ShortName FROM NEI LEFT JOIN SCC ON NEI.SCC=SCC.SCC")
merged_table <- sqldf("SELECT * FROM merged_table WHERE ShortName LIKE '%Highway Veh%' ")

## We only want Baltimore!
justonezip <- merged_table[merged_table$fips=="24510",]

## The chart we want: How have emissions from motor vehicle sources changed from 1999-2008 in Baltimore City? 
plot5data <- aggregate(justonezip$Emissions, by = list(year = justonezip$year), FUN = "sum")

## Spit it into a chart!
png(file="plot5.png")
#qplot(year, x, data=plot4data)
barplot(plot5data$x, names.arg=plot5data$year)
dev.off() 