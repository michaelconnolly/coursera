rankhospital <- function(state, outcome, num = "best") {

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
  
  ## What is the column number for Hospital.Name?
  column_number_hospital_name <- 2
  
  ## convert the right column to numbers.
  data_by_state[, column_number] <- as.numeric(data_by_state[, column_number])
  
  ## Let's remove the NA's.
  bad_rows <- is.na(data_by_state[column_number])
  data_by_state <- data_by_state[!bad_rows, ]
  
  ## Let's sort by column_number, followed by Hospital.Name.
  data_by_state <- data_by_state[ order(data_by_state[,column_number], data_by_state$Hospital.Name), ]
  
  row_number = num
  if (row_number == "best")
    row_number = 1
  else if (row_number == "worst")
    row_number = nrow(data_by_state)
  
  ## if we are asking for a row that is out or range, return NA.
  if (nrow(data_by_state) < row_number){
    NA
    return
  }
  
  ## Let's return the correct row, and the correct column.
  data_by_state[row_number, column_number_hospital_name]
}
