library(ggplot2)

NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

justonezip <- NEI[NEI$fips=="24510",]
plot3data <- aggregate(justonezip$Emissions, by = list(year = justonezip$year, type = justonezip$type), FUN = "sum")
png(file="plot3.png")
qplot(year, x, data=plot3data, facets = . ~ type)
dev.off() 