# Random Selection

# Importing the dataset
dataset = read.csv('Ads_CTR_Optimisation.csv')


# Implementing random selection
N <- 10000
d <- 10

ads_selected <- integer(0)
total_reward <- 0

for (n in 1 : N){
  ad <- sample(c(1:10), 1)
  ads_selected <- append(add_selected, ad)
  reward <- dataset[n, ad]
  total_reward <- total_reward + reward
}

total_reward

# Visualising results - Histogram
hist( ads_selected,
      col = 'blue',
      main = 'Histogram of ads selections',
      xlab = 'Ads',
      ylab = 'Number of time each ad was selected')

