import ray
import modin.pandas as md
df = md.read_csv("esea_master_dmg_demos.part1.csv")

s = time.time()
df = df.fillna(value=0)
e = time.time()
print("Modin Concat Time = {}".format(e-s))