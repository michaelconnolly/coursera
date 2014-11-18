best <- function(state, outcome) {
  
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
  
  ## let's return the first row, which is the minimum, and the value in the hospital name column.
  data_by_state[1, column_number_hospital_name]
}
