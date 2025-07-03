# ---
visualizeEGO <- function(initDesign, initValues, EGOpoints, EGOvalues){
  bestIndex <- which.min(EGOvalues)
  y <- c(initValues, EGOvalues, EGOvalues[bestIndex])
  X <- rbind(initDesign, EGOpoints, EGOpoints[bestIndex, ])
  ninit <- nrow(initDesign)
  nsteps <- nrow(EGOpoints)
  pairs(cbind(y, X), 
        col = c(rep("black", ninit), rep("blue", nsteps), "red"),
        pch = c(rep(1, ninit), rep(19, nsteps + 1)))
}

convergenceEGO <- function(initValues, EGOvalues){
  y0 <- initValues
  plot(c(y0, EGOvalues), main="convergence", 
       xlab = "evaluation number", ylab = "Y values")
  lines(rep(length(y0), 2), range(y0, EGOvalues), lty = 2, col = "gray")
  lines(length(y0) + 0:length(EGOvalues), c(cummin(c(min(y0), EGOvalues))), col="red", lwd=2)
}
