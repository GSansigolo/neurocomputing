#Declare libraries
library(sits)
library(kohonen)
library(inSitu)

#Import file 'br_mt_1_8K_9classes_6bands.rda'
data.tb <- load(file = "/home/sansigolo/Documents/git/Neurocomputing/Projeto/br_mt_1_8K_9classes_6bands.rda")
data.tb <- br_mt_1_8K_9classes_6bands

#Get time series
time_series.ts <- sits_values (data.tb, format = "bands_cases_dates")
write.csv(time_series.ts, file = "time_seriests.csv")

#To use the DTW distance
#sourceCpp(paste(path.package("sits"), "inst/Distances/distance.cpp", sep = "/"))

#Create cluster with Self-organizing maps (kohonen)
# 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 28, 30, 32, 34
koh <-
    sits::sits_kohonen(
        data.tb,
        time_series.ts,
        grid_xdim = 18,
        grid_ydim = 18,
        rlen = 100,
        dist.fcts = "euclidean",
        neighbourhood.fct = "gaussian"
    )

#Analyze the mixture between groups and extract informations about confusion matrix
confusion_by_cluster <- sits_metrics_by_cluster(koh$info_samples)
confusion_matrix <- confusion_by_cluster$confusion_matrix

#Print matrix
confusion_matrix

#Plot matrix
sits_plot_cluster_info(confusion_by_cluster, "Confusion by Cluster")

