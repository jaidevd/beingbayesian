from xml.etree import ElementTree as et  # NOQA: N813

import pandas as pd
from tqdm import tqdm

FIELDS = [
    "AcceptedAnswerId", "AnswerCount", "ClosedDate", "CommentCount",
    "CommunityOwnedDate", "CreationDate", "Id",
    "LastActivityDate", "LastEditDate", "LastEditorDisplayName",
    "LastEditorUserId", "OwnerDisplayName", "OwnerUserId", "ParentId",
    "PostTypeId", "Score", "Tags", "Title", "ViewCount",
]

CHUNK_SIZE = 500_000

file_path = "/media/jaidevd/motherbox/archive/so/Posts.xml"
HALF = 30_000_000
chunks = []
rows = []
n_rows = 0
first_half_done = False

with open(file_path, "rb") as f:
    for event, elem in tqdm(et.iterparse(f, events=("start",)), total=60_371_715):  # NOQA: E501
        if elem.tag == "row":
            rows.append({k: elem.attrib.get(k) for k in FIELDS})
            if len(rows) >= CHUNK_SIZE:
                chunks.append(pd.DataFrame(rows, columns=FIELDS))
                rows = []
                n_rows += CHUNK_SIZE
                if n_rows >= HALF and not first_half_done:
                    df = pd.concat(chunks, ignore_index=True)
                    df.to_parquet("posts_1.parquet", index=False)
                    print(f"Saved {len(df)} rows to posts_1.parquet")
                    chunks = []
                    first_half_done = True
        elem.clear()

if rows:
    chunks.append(pd.DataFrame(rows, columns=FIELDS))

df = pd.concat(chunks, ignore_index=True)
df.to_parquet("posts_2.parquet", index=False)
print(f"Saved {len(df)} rows to posts_2.parquet")
