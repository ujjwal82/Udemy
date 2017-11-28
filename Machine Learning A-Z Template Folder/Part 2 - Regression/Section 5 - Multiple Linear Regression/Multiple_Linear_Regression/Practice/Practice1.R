###
# Create local copy of the dataset
###
#dataset <- as.data.frame(mtcars)
dataset <-as.data.frame(state.x77)

###
# Remove the spaces if any in the column names
###
colnames(dataset) <- gsub(" ", "", colnames(dataset), fixed = TRUE)

###
# Create the formula for linear regression
###

# This might change depending on what dataset we are working on.
dependent_var <- 'LifeExp'  
lm_formula <- as.formula(paste(paste(dependent_var, ' ~', sep = ''), '.'))

###
# Create Linear Regerssion model for all the independent variables
###
regressor <- lm(formula = lm_formula, data = dataset)

###
# Visualization of the model we created.
###
#plot(regressor)

dataset <- subset(dataset, rownames(dataset) != 'Hawaii')
dataset <- subset(dataset, rownames(dataset) != 'South Carolina')
dataset <- subset(dataset, rownames(dataset) != 'Maine')


###
# Looking at the plot "Residuals vs Fitted" we are easily identify 
# Chrysler Imperial
# Toyota Corolla
# Fiat 128
# are the outliers, we will remove them from our dataset
###
dataset <- subset(dataset, rownames(dataset) != 'Chrysler Imperial')
dataset <- subset(dataset, rownames(dataset) != 'Toyota Corolla')
dataset <- subset(dataset, rownames(dataset) != 'Fiat 128')

###
# Looking at the plot "Normal Q-Q" we are easily identify 
# Ford Pantera L
# is additional  outliers, let's remove this also
###
dataset <- subset(dataset, rownames(dataset) != 'Ford Pantera L')


###
# Now we will apply backward elimination  
###

###
# Let apply a while loop to iterate throught the list of clumns and find out 
# the best model for independent variables.
# in every iteration our dependent variable will be mpg
###
factors <- colnames(dataset)
itemToRemove <- dependent_var

plt_adjR_squares <- numeric(0)
plt_lm_formula <- character(0)

while (length(factors) > 2) {
  factors <- factors[!factors == itemToRemove]
  lm_formula <- as.formula(paste(paste(dependent_var, ' ~', sep = ''), 
                                 paste(factors, collapse=" + ", sep = '')))
  plt_lm_formula <- c(plt_lm_formula, paste(paste(dependent_var, ' ~', sep = ''),
                                            paste(factors, collapse=" + ", sep = '')))
  
  regressor <- lm(formula = lm_formula, data = as.data.frame(dataset))
  sum_reg <- summary(regressor)
  plt_adjR_squares <- c(plt_adjR_squares, sum_reg$adj.r.squared)
  
  # find out what all you can get from Summary()
  itemToRemove <- rownames(sum_reg$coefficients)[apply(sum_reg$coefficients , 2, which.max)[4]] 
}

# we have the best LR model with following formula and Adjusted R-Squared value
plt_lm_formula[which(plt_adjR_squares == max(plt_adjR_squares))]
max(plt_adjR_squares)


###
# Now since we have the best Linear Regression model
# Let's apply that and do predictions.
###
lm_formula <- plt_lm_formula[which(plt_adjR_squares == max(plt_adjR_squares))]
regressor <- lm(formula = lm_formula, data = dataset)
summary(regressor)


y_pred <- predict(regressor,newdata = dataset)

# see the predidcted values and actual values and compare
df <- data.frame(cbind(y_pred, dataset[dependent_var]))
colnames(df)

# Visualization of predicted values vs actual values
g_range <- range(0, df$y_pred, df$LifeExp)

plot(df$y_pred, type="o", col="blue", ylim=g_range, 
     axes=FALSE, ann=FALSE)

axis(1, at=1:length(rownames(df)), lab=rownames(df))

axis(2, las=1, at=30*0:g_range[2])

# Create box around plot
box()

lines(df$LifeExp, type="o", pch=22, lty=2, col="red")

# Create a title with a red, bold/italic font
title(main="Predicted vs Actuals", col.main="red", font.main=4)

# Label the x and y axes with dark green text
title(xlab="States", col.lab=rgb(0,0.5,0))
title(ylab="Life Expectancy", col.lab=rgb(0,0.5,0))

# Create a legend at (1, g_range[2]) that is slightly smaller 
# (cex) and uses the same line colors and points used by 
# the actual plots 
legend(1, g_range[2], c("Predicted","Actuals"), cex=0.8, 
       col=c("blue","red"), pch=21:22, lty=2:2);

### ------------------------------------------------------------
## Run the example in '?matplot' or the following:
leg.txt <- c("Setosa     Petals", "Setosa     Sepals",
             "Versicolor Petals", "Versicolor Sepals")
y.leg <- c(4.5, 3, 2.1, 1.4, .7)
cexv  <- c(1.2, 1, 4/5, 2/3, 1/2)
matplot(c(1, 8), c(0, 4.5), type = "n", xlab = "Length", ylab = "Width",
        main = "Petal and Sepal Dimensions in Iris Blossoms")

for (i in seq(cexv)) {
  text  (1, y.leg[i] - 0.1, paste("cex=", formatC(cexv[i])), cex = 0.8, adj = 0)
  legend(3, y.leg[i], leg.txt, pch = "sSvV", col = c(1, 3), cex = cexv[i])
}
### ------------------------------------------------------------- 

# Plot the Adjusted R-squared 
plot(plt_adjR_squares, type="b", col="blue", 
     ylim = range(min(plt_adjR_squares) - 0.05, 0.95),
     axes = FALSE, ann= FALSE)

# Make x axis using Mon-Fri labels
axis(1, at=1:length(plt_adjR_squares), lab=F)

text(axTicks(1), y= 0, srt=45, adj=1,
     labels=plt_adjR_squares,
     xpd=T, cex=1)

# Plot y axis with smaller horizontal labels 
axis(2, las=1, cex.axis=0.8)

# Create box around plot
box()

# Create a title with a red, bold/italic font
title(main="Linear Regression (Best model)", col.main="red", font.main=4)

# Label the x and y axes with dark green text
title(xlab="Formula", col.lab=rgb(0,0.5,0))
title(ylab="R-Squared", col.lab=rgb(0,0.5,0))



