library(ggplot2)

## Load our data!
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

justonezip <- NEI[NEI$fips=="24510",]
plot3data <- aggregate(justonezip$Emissions, by = list(year = justonezip$year, type = justonezip$type), FUN = "sum")
names(plot3data)[3] <- "Emissions"
plot3data$year <- as.character(plot3data$year)

png(file="plot3.png")
qplot(year, data=plot3data, facets = . ~ type) + geom_bar(aes(y=Emissions), stat="identity") + labs(title="Sources of PM25 Emissions in Baltimore City") + theme(axis.text.x = element_text(angle = 90)) 
dev.off() 