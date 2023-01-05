import statistics as st
l1=[10,20,30,40,50,60,70,20]
print("Mean:\n",st.mean(l1))
print("Median:\n",st.median(l1))
print("Mode:\n",st.mode(l1))
print("Harmonic Mean:\n",st.harmonic_mean(l1))
print("Statistics Variance:\n",st.variance(l1))
print(st.median_low([1,2,3,4,5,6]))
print(st.median_low([1,2,3,4,5,6,7,11,-9,-8,-5]))