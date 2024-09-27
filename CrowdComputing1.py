from statistics import mean
from scipy import stats
Estimates=[100,200,300,400,500,600,700,800,900]
Estimates.sort()
m=stats.trim_mean(Estimates,0.1)
print(int(m))
# tv=int(0.1*len(Estimates))
# Estimates=Estimates[tv:]
# Estimates=Estimates[:len(Estimates)-tv]
# print(mean(Estimates))