#---------------------
# Libraries
#---------------------
library(kohonen)
library(RColorBrewer)

#---------------------
# Open Data
#---------------------
poker <- read.csv("/home/sansigolo/Documents/git/Neurocomputing/Laboratorio 2/poker-hand.csv",
sep = ",", header = T, check.names = FALSE)
colnames(poker)

#---------------------
# SOM 1 Config
#---------------------                               sqrt[sqrt(rows*colums)]/2
poker.teste1 <- c("S1","C1","S2","C2","S3","C3","S4","C4","S5","C5")
poker.SOM1 <- som(scale(poker[poker.teste1 ]), grid = somgrid(11, 11, "rectangular"))

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
plot(poker.SOM1, type = "mapping", pchs = 100, main = "Mapping Type SOM")
plot(poker.SOM1, main = "SOM Plot")

#---------------------
# SOM 2 Config
#---------------------
poker.teste2 <- c("S1","C1","S2","C2","S3","C3","S4","C4","S5","C5")

training_indices <- sample(nrow(poker), 25001)
poker.training <- scale(poker[training_indices, poker.teste2])
poker.testing <- scale(poker[-training_indices, poker.teste2], center = attr(poker.training, 
                                                                          "scaled:center"), scale = attr(poker.training, "scaled:scale"))

poker.SOM2 <- xyf(scale(poker[, poker.teste2]), classvec2classmat(poker[, "id"]), 
                grid = somgrid(18, 18, "hexagonal"), rlen = 400)

# Predictions
par(mfrow = c(1, 2))
plot(poker.SOM2, type = "codes", main = c("Codes X", "Codes Y"))
