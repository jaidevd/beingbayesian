"""PostLinks.xml -> duplicate/reference id sets used by the good-question analyses.

Outputs:
  duplicate_ids.npy   : question ids ever marked a duplicate (LinkTypeId 3, PostId)
  dup_target_ids.npy  : canonical targets others were duplicated to (LinkTypeId 3, RelatedPostId)
  link_in_counts.npz  : inbound "Linked" reference counts per post (LinkTypeId 1, RelatedPostId)
"""
from xml.etree import ElementTree as et  # NOQA: N813
from collections import Counter
import numpy as np

POSTLINKS = "/media/jaidevd/motherbox/archive/so/PostLinks.xml"  # <- point at your archive

dups, dup_targets, link_in = set(), set(), Counter()
for _, el in et.iterparse(POSTLINKS, events=("start",)):
    if el.tag == "row":
        t = el.attrib.get("LinkTypeId")
        if t == "3":                       # duplicate
            dups.add(int(el.attrib["PostId"]))
            dup_targets.add(int(el.attrib["RelatedPostId"]))
        elif t == "1":                     # linked
            link_in[int(el.attrib["RelatedPostId"])] += 1
    el.clear()

np.save("duplicate_ids.npy", np.array(sorted(dups), dtype="int64"))
np.save("dup_target_ids.npy", np.array(sorted(dup_targets), dtype="int64"))
np.savez("link_in_counts.npz",
         ids=np.fromiter(link_in.keys(), dtype="int64"),
         counts=np.fromiter(link_in.values(), dtype="int64"))
print(f"duplicates={len(dups):,}  dup_targets={len(dup_targets):,}  linked_posts={len(link_in):,}")
