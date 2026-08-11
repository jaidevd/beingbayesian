from xml.etree import ElementTree as et
import pandas as pd

ids, cd, lad, rep = [], [], [], []
n = 0
for ev, el in et.iterparse("/media/jaidevd/motherbox/archive/so/Users.xml",
                           events=("start",)):
    if el.tag == "row":
        n += 1
        i = int(el.attrib["Id"])
        if i >= 0:  # skip negative-Id "Collectives" (OpenAI, PHP, ...)
            ids.append(i)
            cd.append(el.attrib.get("CreationDate"))
            lad.append(el.attrib.get("LastAccessDate"))
            rep.append(el.attrib.get("Reputation"))
    el.clear()
print("rows", n, "real users", len(ids))
df = pd.DataFrame({"Id": ids, "CreationDate": cd,
                   "LastAccessDate": lad, "Reputation": rep})
df.to_parquet("users.parquet", index=False)
print("wrote users.parquet")
