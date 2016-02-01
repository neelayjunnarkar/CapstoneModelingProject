
#Not simplified, has carrying capacity
LEN = 2000
p0 = .001
K = 1
r = .01
P = array(LEN)
P[1] = p0
for (t in 2:LEN) {
  P[t] = P[t-1] + P[t-1]*((-r/K)*P[t-1] + r)
}

plot(1:LEN, P, type="l")
abline( h = K, col="red") #Carrying Capacity
abline(h = p0, col="blue") #Initial population

