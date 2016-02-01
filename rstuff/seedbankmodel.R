#doesn't work b/c seed growth when pop is 0 is 0

LEN = 1500

K = 1
r = .01
e = 10
seedgrowth = function(pt, st) r*pt*(K-pt)*(st+10*pt)
  
p0 = .001
p = array(LEN)
p[1] = p0

s0 = 0
s = array(LEN)
s[1] = s0

for (t in 1:(LEN-1)) {
  p[t+1] = p[t] + seedgrowth(p[t], s[t])
  s[t+1] = s[t] + e*p[t] - seedgrowth(p[t], s[t])
}

par(mfrow = c(1, 2))

plot(p,type="l", col="blue", main = "Population")
plot(s, type="l", col="red", main="Seed Bank")