## Load our data!
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

## Let's pick up the emission sums for each year.
plot1data <- aggregate(NEI$Emissions, by = list(year = NEI$year), FUN = "sum")

## Bust out the chart.
png(file="plot1.png")
opt <- options("scipen" = 20)
barplot(plot1data$x, names.arg=plot1data$year, main="Total PM25 Emissions in USA")
options(opt)
dev.off()