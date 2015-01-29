library(sqldf)

table1 = read.table("household_power_consumption.txt", header = TRUE, sep = ";", na.strings = "?")
table2 <- sqldf("SELECT * FROM table1 WHERE table1.Date='1/2/2007' OR table1.Date='2/2/2007'")

table3 <- table2
table3$Date <- paste(table3$Date, table3$Time, sep=" ")
table3$Date <- strptime(table3$Date, "%d/%m/%Y %H:%M:%S")


png(filename="plot4.png", width=480, height=480)
par(mfrow = c(2,2))

# First plot.
plot(table3$Date, table3$Global_active_power, type="l", ylab="Global Active Power", xlab="")

# Second plot.
plot(table3$Date, table3$Voltage, type="l", ylab="Voltage", xlab="datetime")

# Third plot
plot(table3$Date, table3$Sub_metering_1, type="l", ylab="Energy sub metering", xlab="")
lines(table3$Date, table3$Sub_metering_2, col="red")
lines(table3$Date, table3$Sub_metering_3, col="blue")
legend("topright", col = c("black", "red", "blue"), bty="n", lty=1, legend = c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"))

# Fourth plot
plot(table3$Date, table3$Global_reactive_power, type="l", ylab="Global_reactive_power", xlab="datetime")

dev.off()

