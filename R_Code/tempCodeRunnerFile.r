library(ggplot2)
require(tidyverse)
print("Hello world", quote = FALSE)


data("mtcars")
cars <- mtcars
print(nrow(cars))
print(head(cars, 10))

x <- c(0:10)
ggplot(data = cars, aes(x = weight, y = hindfoot_length)) +
  geom_point()