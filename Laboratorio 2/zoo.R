#---------------------
# Libraries
#---------------------
library(kohonen)
library(RColorBrewer)

#---------------------
# Open Data
#---------------------
zoo <- read.csv("/home/sansigolo/Documents/git/Neurocomputing/Laboratorio 2/zoo.csv",
sep = ",", header = T, check.names = FALSE)
colnames(zoo)

#---------------------
# SOM 1 Config
#---------------------                               sqrt[sqrt(rows*colums)]
zoo.teste1 <- c("hair","feathers","eggs","milk","airborne","aquatic","predator","toothed","backbone","breathes","venomous","fins","legs","tail","domestic","catsize")
zoo.SOM1 <- som(scale(zoo[zoo.teste1 ]), grid = somgrid(6, 6, "rectangular"))

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
plot(zoo.SOM1, type = "mapping", pchs = 20, main = "Mapping Type SOM")
plot(zoo.SOM1, main = "SOM Plot")

#---------------------
# SOM 2 Config
#---------------------
zoo.teste2 <- c("hair","feathers","eggs","milk","airborne","aquatic","predator","toothed","backbone","breathes","venomous","fins","legs","tail","domestic","catsize")

training_indices <- sample(nrow(zoo), 100)
zoo.training <- scale(zoo[training_indices, zoo.teste2])
zoo.testing <- scale(zoo[-training_indices, zoo.teste2], center = attr(zoo.training, 
                                                                          "scaled:center"), scale = attr(zoo.training, "scaled:scale"))

zoo.SOM2 <- xyf(scale(zoo[, zoo.teste2]), classvec2classmat(zoo[, "type"]), 
                grid = somgrid(6, 6, "hexagonal"), rlen = 300)

# Predictions
par(mfrow = c(1, 2))
plot(zoo.SOM2, type = "codes", main = c("Codes X", "Codes Y"))
