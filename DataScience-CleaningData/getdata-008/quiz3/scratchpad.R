table1new <- read.csv("GDP2.csv", skip=4, na.strings="..", colClasses=c("character", "integer", NA, "Character", "numeric", NA, NA, NA, NA, NA))

table3 <- merge(table1, table2, by.x="X", by.y="CountryCode")
V!
  
  table3 <- merge(table1, table2, by.x="X", by.y="CountryCode")

table4 <- table3[order(table3[5]),]

myFileSlice2 <- myFileSlice[!is.na(myFileSlice$AGS),]