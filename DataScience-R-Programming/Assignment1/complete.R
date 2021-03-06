complete <- function(directory, id = 1:332) {
  
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used
  
  ## Return a data frame of the form:
  ## id nobs
  ## 1  117
  ## 2  1041
  ## ...
  ## where 'id' is the monitor ID number and 'nobs' is the
  ## number of complete cases
  
  ## Let's initialize our output dataframe.
  dataFrameOutput <- data.frame(id=id, nobs=NA)
  
  ## for each monitor, figure out how many complete cases there were and cache it.
  for (i in seq_along(id)){
    
    ## Open the file.
    nameOfFile <- sprintf("%s\\%03d.csv", directory, id[i])
    currentFile <- read.csv(nameOfFile)
    
    ## Let's figure out what columns we want.
    ## to-do: below seems non-optimal with memory usage.  Rewrite for efficiency in the future!
    columnSulfate <- currentFile["sulfate"]
    columnNitrate <- currentFile["nitrate"]
    rowsCompleteCases <- complete.cases(columnSulfate, columnNitrate)
    rowCount <- length(rowsCompleteCases[rowsCompleteCases == TRUE])
    
    ## Store the rowcount in the output dataframe.
    dataFrameOutput[i, "nobs"] <- rowCount
  }
  
  ## We're done, we out.
  dataFrameOutput

#   Example Output:
#
#   source("complete.R")
#   complete("specdata", 1)
#   
#   ##   id nobs
#   ## 1  1  117
#   
#   complete("specdata", c(2, 4, 8, 10, 12))
#   
#   ##   id nobs
#   ## 1  2 1041
#   ## 2  4  474
#   ## 3  8  192
#   ## 4 10  148
#   ## 5 12   96
#   
#   complete("specdata", 30:25)
#   
#   ##   id nobs
#   ## 1 30  932
#   ## 2 29  711
#   ## 3 28  475
#   ## 4 27  338
#   ## 5 26  586
#   ## 6 25  463
#   
#   complete("specdata", 3)
#   
#   ##   id nobs
#   ## 1  3  243
  
}
