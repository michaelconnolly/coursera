pollutantmean <- function(directory, pollutant, id = 1:332) {
  
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'pollutant' is a character vector of length 1 indicating
  ## the name of the pollutant for which we will calculate the
  ## mean; either "sulfate" or "nitrate".
  
  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used

  
  ## Let's create our master numerical values that will cache all the individual files' data.
  sumOfAllNumbers <- 0
  countOfAllNumbers <- 0
  
  ## Let's open each file, suck their aggregate data, and cache it in the master variables.
  for (i in seq_along(id)){
    
    ## Open the file.
    nameOfFile <- sprintf("%s\\%03d.csv", directory, id[i])
    currentFile <- read.csv(nameOfFile)
   
    ## Reduce us down to the rows we want.
    columnNameWeWant <- c(pollutant) 
    columnWeWant <- currentFile[columnNameWeWant]
    rowsWeWant <- columnWeWant[!(is.na(columnWeWant))]

    ## Cache the sums and count of rows.
    currentSum <- sum(rowsWeWant)
    sumOfAllNumbers <- sumOfAllNumbers + currentSum
    currentCount <- length(rowsWeWant)
    countOfAllNumbers <- countOfAllNumbers + currentCount
  }
  
  ## OK, now, let's calculate the final mean.
  finalMean <- sumOfAllNumbers / countOfAllNumbers
  
  ## Let's round to 3 decimal places.
  finalMean <- round(finalMean, digits=3)
  
  ## We're done, we out.
  finalMean
  
  ## Example Output:
  
    ## source("pollutantmean.R")
    
    ## pollutantmean("specdata", "sulfate", 1:10)
    
    ## ## [1] 4.064
    
    ## pollutantmean("specdata", "nitrate", 70:72)
    
    ## ## [1] 1.706
    
    ## pollutantmean("specdata", "nitrate", 23)
    
    ## ## [1] 1.281
}
