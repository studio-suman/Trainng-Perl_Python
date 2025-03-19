# library required for decimal_date() function
library(lubridate)
library(dplyr)

path <- "D:\\OneDrive - Wipro\\Desktop\\AIR\\AIR_WDC_today_Q1Q2Q3.csv"
data <- read.csv(path)

# Filter data for Essential Skills
essential_data <- subset(data, select = c("INDENT_CREATED_ON","ESSENTIAL_SKILL", "NO_OF_RESOURCES") ,ESSENTIAL_SKILL == ".NET")  # Adjust the filter condition if needed # nolint: line_length_linter.

# Create time series object from filtered data
ts_essential <- ts(essential_data$NO_OF_RESOURCES,start = c(2024, 1),frequency = 12)

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
