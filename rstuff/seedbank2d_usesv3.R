LEN <- 43
DISPLAY_LEN <- LEN
WORLD_LEN <- 15

l <- .9 #fraction that lives
e <- 100 #seeds per plant

g_max <- .002 #maximum growth rate of seeds into plants
K <- 1 # carrying capacity

#if Pt > K => g < 0 => decreases those that survive (PROBLEM)
g <- function(Pt) {
  g_max*(1-Pt/K)
}

P <- matrix(nrow=WORLD_LEN, ncol = LEN)
P[1,] = 0.7-


S <- matrix(nrow=WORLD_LEN, ncol=LEN)
S[1,] <- 0 #initial seed bank size

for (t in 1:(LEN-1)) {
  
  P[t+1,] <- l*P[t,] + g(P[t,])*S[t,] + g(P[t,])*e*P[t,]
  S[t+1,] <- S[t,] + e*P[t,]-g(P[t,])*(S[t,]+e*P[t,])
 
}
print(P[4,])