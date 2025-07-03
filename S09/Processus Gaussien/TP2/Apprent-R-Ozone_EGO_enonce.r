rm(list = ls())
source("EGOutils.R")
ozone <- read.table("depSeuil.dat", sep = ",", header = TRUE)
# Vérification du contenu
summary(ozone)

# Changement du type de la variable jour en facteur
ozone[, "JOUR"] <- as.factor(ozone[, "JOUR"])

par(mfrow = c(1, 2))
options(repr.plot.width = 6, repr.plot.height = 3)
hist(ozone[, "O3obs"])
hist(ozone[, "NO2"])

# Même chose pour les autres variables
# hist(ozone[,"MOCAGE"]);hist(ozone[,"TEMPE"]);hist(ozone[,"RMH2O"])
# hist(ozone[,"NO"]);hist(ozone[,"VentMOD"]);hist(ozone[,"VentANG"])

ozone[, "SRMH2O"] <- sqrt(ozone[, "RMH2O"])
ozone[, "LNO2"] <- log(ozone[, "NO2"])
ozone[, "LNO"] <- log(ozone[, "NO"])

ozone <- ozone[, c(1:4, 8:13)]
summary(ozone)
pairs(ozone[, c(3, 4, 6:10)])


set.seed(111) # initialisation du générateur
# Extraction des échantillons
test.ratio <- .2   # part de l'échantillon test
npop <- nrow(ozone) # nombre de lignes dans les données
nvar <- ncol(ozone) # nombre de colonnes
# taille de l'échantillon test
ntest <- ceiling(npop * test.ratio) 
# indices de l'échantillon test
testi <- sample(1:npop, ntest)
# indices de l'échantillon d'apprentissage
appri <- setdiff(1:npop, testi) 

# construction de l'échantillon d'apprentissage
datappr <- ozone[appri, -11] 
# construction de l'échantillon test
datestr <- ozone[testi, -11] 
summary(datappr) # vérification

# construction de l'échantillon d'apprentissage
datappq <- ozone[appri,-2]
# construction de l'échantillon test 
datestq <- ozone[testi,-2] 
summary(datappq) # vérification

# --------------------------------------------------------------

library(e1071)
# SVM avec reglages par defaut
svmDEF <- svm(O3obs ~ ., data = datappr)
svmDEF

# ----------
# QUESTION 1
# ----------
# Creer une fonction cout qui calcule l'erreur par validation croisee
kFoldError <- function(param){
  set.seed(0)   # pour figer les "folds" dans la validation croisee
  obj <- tune.svm(O3obs ~ ., data = datappr,    
                  gamma = param[1], 
                  cost = param[2], 
                  epsilon = param[3])
  return(obj$best.performance)
}


parDEF <- c(svmDEF$gamma, svmDEF$cost, svmDEF$epsilon)
cat("\n(k-fold) error (default model):", 
    round(kFoldError(parDEF), 3),
    "\nCorresponding parameter values:", round(parDEF, 2))

# ----
# Il s'agit de faire mieux que le reglage par defaut,
# avec pas plus de 30 calculs 
# ----

# ----------
# QUESTION 2
# ----------
# Representer la fonction cout contre chaque variable
# En deduire un domaine de recherche pour cost, gamma et epsilon
# Valeur de la fonction cout pour (costOpt, gammaOpt, epsilonOpt) ?
svmTuneCost <- tune.svm(O3obs ~ ., data = datappr,
                        cost = seq(from = 0.5, to = 5, length.out = 6))
plot(svmTuneCost)
costOpt <- as.numeric(svmTuneCost$best.parameters)

gammaOpt <- tune.svm(O3obs ~ ., data = datappr,
                     gamma = seq(from = 0.1, to = 1, length.out = 6))$best.parameters
epsilonOpt <- tune.svm(O3obs ~ ., data = datappr,
                       epsilon = seq(from = 0.1, to = 1, length.out = 6))$best.parameters
parMAR <- c(gammaOpt, costOpt, epsilonOpt)

cat("\n(k-fold) error (marginal optmization):", 
    round(kFoldError(parMAR), 3),
    "\nCorresponding parameter values:", round(parMAR, 2))


# ----------
# QUESTION 3
# ----------
# Creer un plan space-filling à 10 points de type hypercube latin 

n0 <- 10   # budget initial
library(DiceDesign)
X <- lhsDesign(n = n0, dimension = 3)$design
Xopt <- maximinESE_LHS(X, kFoldError, lower = c(0.1, 0.5, 0.1), upper = c(1, 5, 1))  # Utiliser maximinESE_LHS de DiceDesign
X0 <- Xopt$design

lower <- ... # DOMAINE
upper <-  # pour la recherche de (gamma, cost, epsilon)

for (i in 1:ncol(X0)){
  X0[, i] <- lower[i] + X0[, i] * (upper[i] - lower[i]) 
}
pairs(X0)

y0 <- apply(X0, 1, kFoldError)  
bestInitPar <- X0[which.min(y0), ]
cat("\nSmallest (k-fold) error found on X0:", round(min(y0), 3),
    "\nCorresponding parameter values:", round(bestInitPar, 2))

# ----------
# QUESTION 4 
# ----------
# Effectuer 20 iterations de EGO
library(DiceOptim)
km0 <- ...   # Un premier modele de krigeage (avec km de DiceKriging)
km0          # Affichage des parametres
plot(km0)    # Une idee de sa validite

options(warn = - 1)
ego <- EGO.nsteps(...)   # Lancer 20 iterations de EGO

EGOpar <- ego$par
EGOvalue <- ego$value
bestPoint <- which.min(EGOvalue)
bestPar <- EGOpar[bestPoint, ]

cat("\nSmallest (k-fold) error found on additional EGO steps:", 
    round(EGOvalue[bestPoint], 3),
    "\nCorresponding parameter values:", round(EGOpar[bestPoint, ], 2))

# visualisation des points obtenus par EGO
visualizeEGO(initDesign = ..., initValues = ...,
             EGOpoints = ..., EGOvalues = ...)
convergenceEGO(initValues = ..., EGOvalues = ...)

# ----------
# QUESTION 5 
# ----------
# a) Verifier que EGO donne assez souvent la plus petite erreur de validation croisee
# b) L'optimisation marginale (parMAR) donne des resultats quasiment aussi bons que l'optimiseur global (EGO)
# Consequence pour la fonction objectif (que l'on minimise) ?



# ----------
# QUESTION 6 
# ----------
# Que donnent les 4 modeles regles en prediction ? (sur l'ensemble test)
# Que donnent les 4 modeles pour predire le depassement de seuil (> 150) ?

# Creation des modeles
svmMAR <- svm(O3obs ~ ., data = datappr, ...)
svmLHS <- svm(O3obs ~ ., data = datappr, ...)
svmEGO <- svm(O3obs ~ ., data = datappr, ...)

# Calcul de l'erreur quadratique moyenne sur l'echantillon test
RMSEsvmDEF <- mean((predict(svmDEF, newdata = datestr) - datestr[, "O3obs"])^2)
cat("\nRMSE with SVM (default parameters):", RMSEsvmDEF)
...  # A completer pour les 3 autres

# Difference pour la prevision du depassement de seuil > 150 ?
# Matrice de confusion pour la prévision du dépassement de seuil (régression)
print(table(pred.svmr > 150, datestr[, "O3obs"] > 150))
...  # A completer pour les 3 autres

# ----------
# QUESTION 7 
# ----------
# Adapter le TD pour regler un SVM pour classer directement
# selon que le seuil d'ozone est > 150.
# Utiliser le code de wikistat : 
# https://github.com/wikistat/Apprentissage/tree/master/Pic-ozone

# ----------
# QUESTION 8
# ----------
# Adapter le TP pour regler des algorithmes plus difficiles 
# comme le gradient boosting (meme url).