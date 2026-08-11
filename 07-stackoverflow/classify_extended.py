import pandas as pd, numpy as np

top = pd.read_csv("top10k_tags.csv").set_index("tag")["volume"]
base = pd.read_csv("tag_classification_10k.csv").set_index("tag")["cat"].to_dict()  # lang/fw/db-lib/servers
# fix a couple of known misses into existing tech categories
for t in ["swing", "javafx", "awt", "java-awt"]:
    base[t] = "frameworks"

PLATFORMS = set("""android ios iphone ipad windows macos osx linux ubuntu debian centos fedora arch-linux wsl windows-10 windows-11 windows-7 windows-8
cocoa cocoa-touch watchos tvos windows-phone blackberry tizen raspberry-pi arduino embedded embedded-linux cross-platform winapi winapi32 win32 winforms-interop
google-chrome firefox safari internet-explorer microsoft-edge browser mobile android-emulator ios-simulator wear-os""".split())

MARKUP = set("""html css html5 css3 sass scss less xslt xsl svg xaml markdown latex xml xhtml css-selectors flexbox css-grid media-queries
html-table dom mathjax""".split())

TOOLS = set("""git github gitlab bitbucket svn tortoisesvn mercurial version-control docker docker-compose dockerfile kubernetes helm openshift terraform ansible vagrant chef-infra puppet
jenkins github-actions gitlab-ci travis-ci circleci teamcity bamboo azure-pipelines azure-devops maven gradle ant sbt cmake makefile msbuild nuget pip conda pipenv poetry homebrew apt-get
npm yarn pnpm webpack babeljs vite rollupjs parcel gulp grunt eslint prettier
amazon-web-services aws-lambda amazon-s3 amazon-ec2 aws-cli amazon-cloudformation azure azure-functions azure-active-directory google-cloud-platform google-app-engine google-cloud-functions
heroku netlify vercel digital-ocean cloudflare
visual-studio visual-studio-code eclipse intellij-idea android-studio xcode pycharm vim emacs sublimetext atom-editor netbeans jupyter-notebook jupyter ipython google-colaboratory
excel google-sheets google-apps-script wordpress sharepoint salesforce jira ms-word powerpoint outlook vba-excel google-maps google-maps-api-3
.htaccess ssh curl postman fiddler wireshark nginx-config""".split())

def classify(t):
    if t in base: return base[t]
    if t in PLATFORMS: return "platforms"
    if t in MARKUP: return "markup-and-styling"
    if t in TOOLS: return "tools-and-infrastructure"
    return "concepts"   # catch-all topic axis (top-10k only)

cls = {t: classify(t) for t in top.index}
pd.Series(cls, name="cat").rename_axis("tag").to_csv("tag_classification_extended.csv")

df = top.reset_index(); df["cat"] = df["tag"].map(cls)
cov = df.groupby("cat").agg(n=("tag","size"), vol=("volume","sum"))
cov["vol_pct"] = (100*cov["vol"]/df["volume"].sum()).round(1)
print("=== extended taxonomy coverage (top 10k) ===")
print(cov.sort_values("vol", ascending=False).to_string())

# collapse per category
s = pd.read_parquet("tag_month_counts.parquet")["n"].reset_index()
s["month"]=s["month"].dt.to_timestamp(); s["cat"]=s["tag"].map(cls)
cat = s.dropna(subset=["cat"]).groupby(["month","cat"])["n"].sum().unstack("cat")
pre=cat.loc["2022-01-01":"2022-09-01"].mean(); now=cat.loc["2025-07-01":].mean()
print("\n=== collapse by category (2022 -> 2025) ===")
for c in cat.columns.sort_values():
    print(f"  {c:26s} -{(1-now[c]/pre[c])*100:.1f}%")
cat.to_csv("tag_categories_extended.csv")
