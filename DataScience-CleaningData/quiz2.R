myload_question1 <- function() {
  
  
  library("httr")
  library("RJSONIO")
  
  myapp = oauth_app("github", key="822ab0e81c9ee87e4e81", secret="cb63010c31b7fa173ee0c19013a34f7d19f57a8f")
  sig = sign_oauth1.0(myapp, token = "822ab0e81c9ee87e4e81", token_secret = "cb63010c31b7fa173ee0c19013a34f7d19f57a8f")
  mydoc = GET("https://api.github.com/users/jtleek/repos")  
    
  json1 = content(mydoc)
  json2 = jsonlite::fromJSON(toJSON(json1))
    
  json3 = json2[json2$name=="datasharing",]
  x = json3$created_at
  
  }

myload_question2 <- function() {
  
  library("sqldf")
  
  acs <- read.csv("getdata_data_ss06pid.csv", colClasses = "character")
 
  
  
}

myload_question4 <- function() {
  myfile <- download.file("http://biostat.jhsph.edu/~jleek/contact.html", "contact.html")
  
  con = url("http://biostat.jhsph.edu/~jleek/contact.html")
  myhtml <<- readLines(con)
  close(con)
}

myload_question5 <- function(){
  myfile <- download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for", "wksst8110.for")
  mytable <- read.fwf("wksst8110.for", skip=4, widths=c(12, 7,4, 9,4, 9,4, 9,4))
)
  
 
  
  
}