library(ggplot2)
library(sqldf)

## Load our data!
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

## Fix column names so later transformations work.
names(SCC)[3] <- "ShortName"
names(SCC)[4] <- "EISector"

## add the activities labels and merge up the training data.
table_plot6 <- sqldf("SELECT NEI.*, SCC.ShortName FROM NEI LEFT JOIN SCC ON NEI.SCC=SCC.SCC")
table_plot6 <- sqldf("SELECT * FROM table_plot6 WHERE ShortName LIKE '%Highway Veh%' ")

## We only want Baltimore!
##justtwozip <- merged_table[merged_table$fips=="24510" OR merged_table$fips=="06037",]
table_plot6 <- sqldf("SELECT * FROM table_plot6 WHERE fips='24510' OR fips='06037'")

## The chart we want: 
## 6.Compare emissions from motor vehicle sources in Baltimore City with emissions from motor vehicle sources
## in Los Angeles County, California (fips == "06037"). Which city has seen greater changes over time
## in motor vehicle emissions
plot6data <- aggregate(table_plot6$Emissions, by = list(year = table_plot6$year, zip = table_plot6$fips), FUN = "sum")

## Spit it into a chart!
png(file="plot6.png")
#qplot(year, x, data=plot4data)
#barplot(plot6data$x, names.arg=plot6data$year)
qplot(year, x, data=plot6data, facets = . ~ zip)
dev.off() 