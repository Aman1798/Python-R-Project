# Load necessary libraries
library(datasets)
library(ggplot2)

# Load built-in dataset 'iris'
data(iris)  

# Show first few rows of the iris dataset
head(iris)    

# Summary statistics of the iris dataset
summary(iris)   

# Plot the iris dataset
plot(iris)

# Detach the datasets package to avoid conflicts
detach("package:datasets", unload = TRUE)

# Clear any existing plots if there is one
if (!is.null(dev.list())) dev.off()  

# Clear the console
cat("\014")

# Exploratory Data Analysis (EDA) and Visualization of the Iris Dataset

# Plotting categorical variable (Species)
plot(iris$Species) 

# Plotting quantitative variable (Petal Length)
plot(iris$Petal.Length) 

# Plotting categorical vs quantitative variable (Species vs Petal Width)
plot(iris$Species, iris$Petal.Width) 

# Plotting two quantitative variables (Petal Length vs Petal Width)
plot(iris$Petal.Length, iris$Petal.Width)

# Customizing plot appearance for Petal Length vs Petal Width
plot(iris$Petal.Length, iris$Petal.Width,
     col = "#cc0000", # red color
     pch = 19,        # solid circles for points
     main = "Iris: Petal Length vs Petal Width",
     xlab = "Petal Length",
     ylab = "Petal Width")

# Plotting functions
plot(cos, 0, 2*pi)   # Cosine function
plot(exp, 1, 5)       # Exponential function
plot(dnorm, -3, +3)   # Density of normal distribution

# Customizing plot appearance for density plot
plot(dnorm, -3, +3,
     col = "#cc0000",
     lwd = 5,           # Line Width
     main = "Standard Normal Distribution",
     xlab = "Z-scores",
     ylab = "Density")

# Scatter plot for multivariate data
plot(iris)

# Mix of continuous and categorical variables for Petal Length
print(iris$Petal.Length)
hist(iris$Petal.Length, breaks = 50)
table(iris$Petal.Length)

# Mix of continuous and categorical variables for Species
print(iris$Species)
table(iris$Species)

# Scatter plot for Petal Length vs Species
matplot(as.numeric(iris$Species), iris$Petal.Length, 
        col = "blue", pch = 19, xlab = "Species", ylab = "Petal length")

# Introduction to ggplot2 for advanced plotting

# Scatter plot using ggplot2
ggplot(data = iris, mapping = aes(x = Species, y = Petal.Length)) + 
  geom_point(col = "red") +
  labs(x = "Species", y = "Petal length", title = "Continuous vs Categorical") + 
  theme(plot.title = element_text(hjust = 0.5, face = "bold", size = 16)) +
  theme(axis.text = element_text(size = 12, face = "bold"),
        axis.title = element_text(size = 14, face = "bold"))

# Boxplot using ggplot2
ggplot(iris, aes(x = Species, y = Petal.Length)) + 
  stat_boxplot(geom = 'errorbar', width = 0.25) + 
  geom_boxplot()
