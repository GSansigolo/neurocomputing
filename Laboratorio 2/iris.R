#---------------------
# Libraries
#---------------------
library(kohonen)
library(RColorBrewer)

#---------------------
# Open Data
#---------------------
iris <- read.csv("/home/sansigolo/Documents/git/Neurocomputing/Laboratorio 2/iris.csv",
sep = ",", header = T, check.names = FALSE)
colnames(iris)

#---------------------
# SOM 1 Config
#---------------------                               sqrt[sqrt(rows*colums)]
iris.teste1 <- c("sepal_length", "sepal_width", "petal_length", "petal_width")
iris.SOM1 <- som(scale(iris[iris.teste1 ]), grid = somgrid(5, 5, "rectangular"))

#---------------------
# Plots
#---------------------

# Heat Colors
#colors <- function(n, alpha = 1) {
#  rev(heat.colors(n, alpha))
#}

# Heat Plot
#plot(iris.SOM1, type = "counts", palette.name = colors, heatkey = TRUE)

# Toroidal Plot                         
par(mfrow = c(1, 2))
plot(iris.SOM1, type = "mapping", pchs = 20, main = "Mapping Type SOM")
plot(iris.SOM1, main = "SOM Plot")

#---------------------
# SOM 2 Config
#---------------------
iris.teste2 <- c("sepal_length", "sepal_width", "petal_length", "petal_width")

training_indices <- sample(nrow(iris), 100)
iris.training <- scale(iris[training_indices, iris.teste2])
iris.testing <- scale(iris[-training_indices, iris.teste2], center = attr(iris.training, 
                                                                          "scaled:center"), scale = attr(iris.training, "scaled:scale"))

iris.SOM2 <- xyf(scale(iris[, iris.teste2]), classvec2classmat(iris[, "species"]), 
                grid = somgrid(5, 5, "hexagonal"), rlen = 300)

# Predictions
par(mfrow = c(1, 2))
plot(iris.SOM2, type = "codes", main = c("Codes X", "Codes Y"))

## use hierarchical clustering to cluster the codebook vectors
groups = 3
iris.hc = cutree(hclust(dist(iris.som$codes)), groups)

#cluster boundaries
add.cluster.boundaries(iris.som, iris.hc)