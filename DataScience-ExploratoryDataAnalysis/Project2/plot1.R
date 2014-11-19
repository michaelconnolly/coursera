NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

plot1data <- aggregate(NEI$Emissions, by = list(year = NEI$year), FUN = "sum")

png(file="plot1.png")
barplot(plot1data$x, names.arg=plot1data$year)
dev.off()