A <- 7
B <- 0.1
a <- 1/2
b <- pi^4/5

ishigamiFun <- function(x){
  sin(x[,1]) + A * sin(x[,2])^2 + B * x[,3]^4 * sin(x[,1])
}

N <- 1000
xSim <- matrix(runif(3*N, -pi, pi), ncol=3)
ySim <- ishigamiFun(xSim)
ySimCentered <- ySim - mean(ySim)

i <- 1
xi <- ySimCentered[,i]
plot(xi, ySimCentered, xlim=c(-pi, pi), cex=0.2)
t <- seq(from=-pi, to=pi, length=200)

loessModel <- loess(y - x, data=data.frame(x=xi, y=ySimCentered))
mainHat <- predict(loessModel, data.frame(x=t))

lines(t, mainHat, col="blue", lwd=4)
lines(t, sin(t)*(1+B*b), col="red", lwd=1)
lines(t, A*(sin(t)^2-a), col="red", lwd=1)