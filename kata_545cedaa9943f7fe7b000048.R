# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

is_pangram <- function(s){
  all(letters %in% unlist(strsplit(tolower(s), "")))
}
