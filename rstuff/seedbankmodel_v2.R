LEN = 1500
 
seed_growth_max = .0009
K = 1 #carrying capacity
e = 12 #seeds per plant

seed_growth = function(pt, st) seed_growth_max*(1-pt/K)*(st+e*pt)



p0 = .001
p = array(LEN) # population size
s = array(LEN) # seed bank size

p[1] = p0

for (t in 1:(LEN-1)) {
  p[t+1] = p[t] + seed_growth(p[t], s[t])
  s[t+1] = s[t] + e*p[t] - (seed_growth(p[t], s[t]))
}
par(mfrow = c(1, 2))

plot(p,type="l", col="blue", main = "Population")
plot(s, type="l", col="red", main="Seed Bank")