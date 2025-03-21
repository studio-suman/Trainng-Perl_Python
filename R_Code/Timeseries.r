# library required for decimal_date() function
library(lubridate)
library(dplyr)
library(forecast)
library(tseries)
library(ggplot2)

path <- "D:\\OneDrive - Wipro\\Desktop\\AIR\\AIR_WDC_today_Q1Q2Q3.csv"
data <- read.csv(path)

# Filter data for Essential Skills
essential_data <- subset(data, select = c("INDENT_CREATED_ON","ESSENTIAL_SKILL", "NO_OF_RESOURCES"),ESSENTIAL_SKILL == ".NET")  # Adjust the filter condition if needed # nolint: line_length_linter.

# Convert the date to decimal date format
essential_data$INDENT_CREATED_ON <-
  as.Date(essential_data$INDENT_CREATED_ON, format = "%Y-%m-%d")
# essential_data$INDENT_CREATED_ON <-
#  decimal_date(essential_data$INDENT_CREATED_ON)

essential_data <- essential_data[order(essential_data$INDENT_CREATED_ON), ]

# Sum the data on No of resources
total_resources <- essential_data %>%
  group_by(INDENT_CREATED_ON) %>%
  summarise(TOTAL_RESOURCES = sum(NO_OF_RESOURCES))

# Convert the date to a time series object

ts_essential <- ts(total_resources$TOTAL_RESOURCES, start = c(year(min(essential_data$INDENT_CREATED_ON)),
                           month(min(essential_data$INDENT_CREATED_ON))), frequency = 12) # nolint: line_length_linter.


# Check if the time series is stationary
adf_test <- adf.test(ts_essential)
print(adf_test)

# If the time series is not stationary,
#perform differencing to make it stationary
if (adf_test$p.value > 0.05) {
  ts_essential <- diff(ts_essential)
  adf_test <- adf.test(ts_essential)
  print(adf_test)
}


# Create the plot with better formatting
plot(ts_essential,
     main = "Time Series of Essential Skills Resources",
     xlab = "Time",
     ylab = "Number of Resources",
     col = "blue",
     lwd = 2)

# Add grid for better readability
grid()

# Basic statistics of the filtered data
print(summary(ts_essential))

model <- auto.arima(ts_essential)
print(summary(model))


# Create the plot with better formatting
plot(forecast(model, h=20),
     main = "Time Series of Essential Skills Resources",
     xlab = "Time",
     ylab = "Number of Resources",
     col = "orange",
     lwd = 2)

suman <- forecast(model, h=30)
data.frame(suman)
