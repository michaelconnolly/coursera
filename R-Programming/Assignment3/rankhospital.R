rankhospital <- function(state, outcome, num = "best") {
  ## Read outcome data
  ## Check that state and outcome are valid
  ## Return hospital name in that state with the given rank
  ## 30-day death rate


  
  ## Read outcome data
  data_all <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  ## Check that state is valid
  ## Logic for validity: if it is in the table.
  data_by_state <- data_all[data_all$State == state, ]
  if (nrow(data_by_state) == 0){
    stop("invalid state")
  }
    
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
  ## data_by_state_and_outcome <- data_by_state[data_by_state[]]
  
  ## Let's remove the NA's.
  bad_rows <- is.na(data_by_state[column_number])
  data_by_state_clean <- data_by_state[!bad_rows, ]
  
  ## What is the lowest value?
  lowest_value <- as.numeric(mapply(min, data_by_state_clean[column_number]))
  data_lowest_value <- data_by_state_clean[data_by_state_clean[column_number] == lowest_value, ]
  
  ## TODO!  Need to sort and show the least alphabetical!
  
  ## Pull out the row that has the lowest value.
  ##data_min <- lapply(data_by_state_clean, min)
  
  ## Return hospital name in that state with lowest 30-day death
  data_lowest_value$Hospital.Name
  
  ## rate
}
