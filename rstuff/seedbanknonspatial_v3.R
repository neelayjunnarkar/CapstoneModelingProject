#NonSpatial SeedBank Model
#Does not work because SeedBank Size can go below 0
#Problem is that for some reason the contents of the arrays are registered as NaN, so conditionals do not work
LEN <- 43
DISPLAY_LEN <- LEN

l <- .9 #fraction that lives
e <- 100 #seeds per plant

g_max <- .002 #maximum growth rate of seeds into plants
K <- 1 # carrying capacity

#if Pt > K => g < 0 => decreases those that survive (PROBLEM)
g <- function(Pt) {
  g_max*(1-Pt/K)
}

P <- array(data = 0, dim=LEN);
P[1] <- .01 #initial plant population

S <- array(data = 0, dim=LEN);
S[1] <- 0 #initial seed bank size

for (t in 1:(LEN-1)) {

  P[t+1] <- l*P[t] + g(P[t])*S[t] + g(P[t])*e*P[t]
  S[t+1] <- S[t] + e*P[t]-g(P[t])*(S[t]+e*P[t]) 

 # if (S[t+1] < 0) {
 #   S[t+1] <- 0
 # }
#  if (P[t+1] <= 0) {
 #   P[t+1] <- 0;
#  }

  if(t> 35) {
    cat("t: ", t, " P: ", P[t+1], " S: ", S[t+1], '\n')
  }

}

par(mfrow=c(1, 2))
plot(x=1:DISPLAY_LEN, y=P[1:DISPLAY_LEN], type="l", col="blue");
plot(x=1:DISPLAY_LEN, y=S[1:DISPLAY_LEN], type="l", col="red")