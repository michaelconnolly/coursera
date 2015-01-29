library(sqldf)

table1 = read.table("household_power_consumption.txt", header = TRUE, sep = ";", na.strings = "?")
table2 <- sqldf("SELECT * FROM table1 WHERE table1.Date='1/2/2007' OR table1.Date='2/2/2007'")


table3 <- table2
table3$Date <- paste(table3$Date, table3$Time, sep=" ")
table3$Date <- strptime(table3$Date, "%d/%m/%Y %H:%M:%S")

png(filename="plot2.png", width=480, height=480)
plot(table3$Date, table3$Global_active_power, type="l", ylab="Global Active Power (kilowatts)", xlab="")
dev.off()

