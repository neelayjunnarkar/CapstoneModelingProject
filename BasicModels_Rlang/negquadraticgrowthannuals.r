LEN = 20000
p0 = .01
K = 1
P = array(LEN)
r = .01

P[1] = p0

for (t in 2:LEN) {
  P[t] = P[t-1]+P[t-1]^2*(K-P[t-1])*r
}
  
plot(1:LEN, P, type = "l")
abline( h = K, col="red") #Carrying Capacity
abline(h = p0, col="blue") #Initial population