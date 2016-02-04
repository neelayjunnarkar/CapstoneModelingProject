 
K = 1
r = .01
overallgrowth = function(pt) r*pt*(K-pt)

LEN = 2500
p0 = .000001
p = array(LEN)
p[1] = p0

for (t in 1:(LEN-1)) {
  p[t+1] = p[t] + overallgrowth(p[t])
}

plot(p, type="l")