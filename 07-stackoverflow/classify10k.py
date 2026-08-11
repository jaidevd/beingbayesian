import pandas as pd, numpy as np, re

top = pd.read_csv("top10k_tags.csv").set_index("tag")["volume"]

LANG = set("""javascript python java c# php c++ c r swift objective-c ruby typescript vba bash scala kotlin vb.net dart matlab powershell shell sql perl go rust
t-sql pl-sql plsql plpgsql awk sed tcl zsh fish batch-file cmd vbscript jscript applescript autohotkey autoit
haskell clojure clojurescript elixir erlang f# ocaml lua julia groovy cobol fortran fortran90 fortran77 pascal delphi object-pascal prolog scheme lisp common-lisp emacs-lisp racket crystal nim zig assembly x86 x86-64 arm mips vhdl verilog systemverilog apl abap actionscript actionscript-3 coffeescript elm purescript reason reasonml solidity sas stata spss smalltalk ada haxe vala octave sml standard-ml idris coq forth
python-3.x python-2.7 python-2.x c++11 c++17 c++14 c++20 c++03 java-8 java-11 php-7 php-8 swift3 swift4 swift5 es6 ecmascript-6 typescript-generics
groovy kotlin-multiplatform""".split())

FRAMEWORK = set("""angular angularjs angular2 react-native vue.js vuejs2 vuejs3 svelte sveltekit django flask fastapi ruby-on-rails ruby-on-rails-3 ruby-on-rails-4 ruby-on-rails-5 laravel laravel-5 laravel-8 symfony symfony4 symfony5 codeigniter cakephp yii yii2 zend-framework
spring spring-boot spring-mvc spring-security spring-data-jpa spring-webflux spring-data struts struts2 jsf primefaces play-framework grails micronaut quarkus ktor vert.x
asp.net asp.net-mvc asp.net-core asp.net-web-api asp.net-mvc-4 asp.net-mvc-3 asp.net-core-mvc asp.net-core-webapi blazor .net .net-core .net-6.0 .net-5 entity-framework entity-framework-core ef-core-6.0
xamarin xamarin.forms maui wpf winforms uwp qt qt5 pyqt pyqt5 pyside gtk gtk3 electron flutter ionic ionic-framework cordova phonegap nativescript swiftui jetpack-compose android-jetpack-compose combine
express nestjs next.js nuxt.js gatsby ember.js backbone.js knockout.js meteor aurelia hapi.js koa sails.js tornado web2py pyramid bottle
hibernate jpa mybatis
unity-game-engine unity3d unreal-engine cocos2d libgdx pygame kivy""".split())

LIBRARY = set("""jquery jquery-ui jquery-mobile lodash underscore.js pandas numpy scipy matplotlib seaborn plotly scikit-learn scikit-image tensorflow tensorflow2.0 keras pytorch theano caffe mxnet xgboost lightgbm
opencv pillow python-imaging-library requests beautifulsoup beautifulsoup4 scrapy axios moment momentjs date-fns d3.js three.js chart.js highcharts echarts leaflet
bootstrap twitter-bootstrap bootstrap-4 bootstrap-5 tailwind-css bulma materialize material-ui mui ant-design chakra-ui semantic-ui
redux react-redux mobx rxjs vuex ngrx redux-toolkit jackson gson retrofit okhttp boost eigen sfml sdl sdl-2 ggplot2 dplyr tidyverse shiny data.table stringr lubridate purrr caret tidyr
selenium selenium-webdriver puppeteer playwright cypress jest mocha jasmine karma junit junit5 pytest rspec nunit xunit testng mockito
log4j logback slf4j log4net serilog nlog apache-poi itext jsoup cheerio socket.io signalr styled-components formik react-hook-form immer polars
reactjs react-hooks jestjs enzyme react-router vue-router material-ui react-testing-library""".split())

SERVER = set("""apache apache2 httpd nginx tomcat apache-tomcat tomcat7 tomcat8 iis iis-7 iis-7.5 jetty gunicorn uwsgi mod-wsgi node.js kestrel wildfly jboss jboss7 glassfish websphere weblogic caddy lighttpd haproxy varnish wsgi fastcgi php-fpm passenger puma unicorn thin webrick""".split())

DATABASES = set("""mysql postgresql postgres mongodb sql-server sqlite sqlite3 oracle oracle-database database databases relational-database nosql
redis mariadb cassandra couchdb neo4j dynamodb amazon-dynamodb elasticsearch influxdb ms-access db2 google-bigquery bigquery snowflake-cloud-data-platform
h2 hsqldb firebird sql-server-2008 sql-server-2012 sql-server-2014 sql-server-2016 sql-server-2008-r2 sql-server-2005 sql-server-2017
realm indexeddb cosmosdb azure-cosmosdb memcached rethinkdb arangodb clickhouse cockroachdb firebase firebase-realtime-database google-cloud-firestore
sqlalchemy pymongo mongoose psycopg2 jdbc odbc pdo""".split())
LIBRARY |= DATABASES

cat = {}
for c, s in [("languages", LANG), ("frameworks", FRAMEWORK), ("databases-and-libraries", LIBRARY), ("servers", SERVER)]:
    for t in s:
        cat[t] = c

top_df = top.reset_index()
top_df["cat"] = top_df["tag"].map(cat)
classified = top_df.dropna(subset=["cat"])
print("=== coverage over top 10k ===")
print("tags classified: %d / 10000" % len(classified))
print("volume classified: %.1f%% of top-10k volume" % (100*classified["volume"].sum()/top_df["volume"].sum()))
print(classified.groupby("cat").agg(n=("tag","size"), vol=("volume","sum")).assign(vol_pct=lambda x:(100*x["vol"]/top_df["volume"].sum()).round(1)))

print("\n=== top 40 UNCLASSIFIED tags (what we're leaving out) ===")
unc = top_df[top_df["cat"].isna()].head(40)
print(unc[["tag","volume"]].to_string(index=False))

# which of my list entries never matched a top-10k tag (spelling/absent)
listed = set(cat)
matched = set(classified["tag"])
print("\n=== list entries NOT found in top-10k (spelling or too rare) ===")
print(sorted(listed - matched))
pd.Series(cat, name="cat").rename_axis("tag").to_csv("tag_classification_10k.csv")
