# Hierarchical Clustering

dataset <- read.csv("Mall_Customers.csv")
X <- dataset[,4:5]

# Using dendogram to find the optimal number of clusters
dendogram = hclust(d = dist(X, method = "euclidean"), method = "ward.D")

plot(dendogram,
     main = "Dendogram",
     xlab = "Customers",
     ylab = "Euclidean distance")

# Apply Hierarchical clustering to the mall dataset
hc = hclust(d = dist(X, method = "euclidean"), method = "ward.D")
y_hc = cutree(hc, k = 5)


# Visulizing the clusters
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste("Clusters of clients"),
         xlab = "Annual income (K$)",
         ylab = "spending score (1-100)")

