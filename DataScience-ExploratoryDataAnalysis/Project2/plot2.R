NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

justonezip <- NEI[NEI$fips=="24510",]
plot2data <- aggregate(justonezip$Emissions, by = list(year = justonezip$year), FUN = "sum")

png(file="plot2.png")
barplot(plot2data$x, names.arg=plot2data$year)
dev.off()