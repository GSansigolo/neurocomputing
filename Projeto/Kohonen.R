##Libraries
library(sits)
library(kohonen)
library(inSitu)

##Import
data.tb <- load(file = "/home/sansigolo/Documents/git/Neurocomputing/Projeto/br_mt_1_8K_9classes_6bands.rda")
data.tb <- br_mt_1_8K_9classes_6bands

#Get time series
time_series.ts <- sits_values (data.tb, format = "bands_cases_dates")

##To use the DTW distance
#sourceCpp(paste(path.package("sits"), "inst/Distances/distance.cpp", sep = "/"))

#Create cluster with Self-organizing maps (kohonen)
koh <-
    sits::sits_kohonen(
        data.tb,
        time_series.ts,
        grid_xdim = 25,
        grid_ydim = 25,
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

