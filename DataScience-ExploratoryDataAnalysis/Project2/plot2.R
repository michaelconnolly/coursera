## Load our data!
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

## Filter down to Baltimore city, then grab the sums of each year.
justonezip <- NEI[NEI$fips=="24510",]
plot2data <- aggregate(justonezip$Emissions, by = list(year = justonezip$year), FUN = "sum")

png(file="plot2.png")
barplot(plot2data$x, names.arg=plot2data$year)
dev.off()
## Bust out the chart.
png(file="plot2.png")
opt <- options("scipen" = 20)
barplot(plot2data$x, names.arg=plot2data$year, main="Total PM25 Emissions in Baltimore City")
options(opt)
dev.off()