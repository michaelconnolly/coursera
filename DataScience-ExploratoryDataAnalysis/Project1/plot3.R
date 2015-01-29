library(sqldf)

table1 = read.table("household_power_consumption.txt", header = TRUE, sep = ";", na.strings = "?")
table2 <- sqldf("SELECT * FROM table1 WHERE table1.Date='1/2/2007' OR table1.Date='2/2/2007'")


table3 <- table2
table3$Date <- paste(table3$Date, table3$Time, sep=" ")
table3$Date <- strptime(table3$Date, "%d/%m/%Y %H:%M:%S")

png(filename="plot3.png", width=480, height=480)
plot(table3$Date, table3$Sub_metering_1, type="l", ylab="Energy sub metering", xlab="")
lines(table3$Date, table3$Sub_metering_2, col="red")
lines(table3$Date, table3$Sub_metering_3, col="blue")
legend("topright", col = c("black", "red", "blue"), lty=1, legend = c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"))
dev.off()

