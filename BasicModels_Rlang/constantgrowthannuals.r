LEN = 100
p0 = .1
P = array(LEN)
P[1] = p0;
r = 1.9


for (t in 2:LEN) {
  P[t] = P[t-1]+r*P[t-1];
}
plot(1:LEN, P, type="l")