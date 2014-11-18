rankall <- function(outcome, num = "best") {
  
  ## Read outcome data
  data_all <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  ## Check that outcome are valid, and get further subset.
  column_number <- -1
  if (outcome == "heart attack"){
    column_number <- 11
  }
  else if (outcome == "heart failure"){
    column_number <- 17
  }
  else if (outcome == "pneumonia"){
    column_number <- 23
  }
  else{
    stop("invalid outcome")
  }
  
  ## What is the column number for Hospital.Name?
  column_number_hospital_name <- 2
  
  ## convert the right column to numbers.
  data_all[, column_number] <- as.numeric(data_all[, column_number])
  
  ## Let's remove the NA's.
  bad_rows <- is.na(data_all[column_number])
  data_all <- data_all[!bad_rows, ]
  
  ## Let's sort by column_number, followed by Hospital.Name.
  data_all <- data_all[ order(data_all[,column_number], data_all$Hospital.Name), ]
  
  ## let's split the dataset into different states.
  data_split <- split(data_all, data_all$State)
  
  ## Let's create a function that can be applied to each group
  ## and return the right row.
  get_row <- function(myDataSet){
    row_number = num
    if (row_number == "best")
      row_number = 1
    else if (row_number == "worst")
      row_number = nrow(myDataSet)
    
    if (nrow(data_all) < row_number){
      NA
    return
    }
    
    return_value <- myDataSet[row_number, column_number_hospital_name]
    return_value
  }

  ## Let's return the collection of correct rows.
  data_output <- lapply(data_split, get_row)
  
  ## let's create a dataframe with the right data.
  data_output2 <- data.frame(hospital=unlist(data_output), state=names(data_output))

  data_output2
}