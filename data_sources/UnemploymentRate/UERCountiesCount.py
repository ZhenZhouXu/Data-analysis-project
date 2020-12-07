import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()
data = sc.textFile(sys.argv[1], 1).mapPartitions(lambda x: reader(x))

result = data.sortBy(lambda x: x[0])
outputTotal = result.map(lambda x: x[0] + "," + x[1] + "-" + x[2] + "," + x[6])
outputTotal.saveAsTextFile("UERCountiesCount.out")

#for each county
AlbanyCounty = result.filter(lambda x: "Albany County" in x).map(lambda x: x[1] + "-" + x[2] + "," + x[6])
AlbanyCounty.saveAsTextFile("UERAlbanyCounty.out")
#
# AlleganyCounty = result.filter(lambda x: "Allegany County" in x).map(lambda x: x[1] + "-" + x[2] + "," + x[6])
# AlleganyCounty.saveAsTextFile("UERAlleganyCounty.out")
#
# BronxCounty = result.filter(lambda x: "Bronx County" in x).map(lambda x: x[1] + "-" + x[2] + "," + x[6])
# BronxCounty.saveAsTextFile("UERBronxCounty.out")
#
# BroomeCounty = result.filter(lambda x: "Broome County" in x).map(lambda x: x[1] + "-" + x[2] + "," + x[6])
# BroomeCounty.saveAsTextFile("UERBroomeCounty.out")
#
# CattaraugusCounty = result.filter(lambda x: "Cattaraugus County" in x).map(lambda x: x[1] + "-" + x[2] + "," + x[6])
# CattaraugusCounty.saveAsTextFile("UERCattaraugusCounty.out")
#
# CayugaCounty = result.filter(lambda x: "Cayuga County" in x).map(lambda x: x[1] + "-" + x[2] + "," + x[6])
# CayugaCounty.saveAsTextFile("UERCayugaCounty.out")



'''
Cols:
"AREA", 0
"YEAR",  1
"MONTH", 2
"LABORFORCE", 3
"EMP", 4
"UNEMP", 5
"UNEMPRATE" 6

    
module load python/gnu/3.6.5
module load spark/2.4.0

rm -rf UERCountiesCount.out
rm -rf UERAlbanyCounty.out


hfs -rm -R UERCountiesCount.out
hfs -rm -R UERAlbanyCounty.out


spark-submit --conf \
spark.pyspark.python=/share/apps/python/3.6.5/bin/python \
UERCountiesCount.py countiesUER.csv

hfs -getmerge UERCountiesCount.out UERCountiesCount.out
hfs -getmerge UERAlbanyCounty.out UERAlbanyCounty.out



hfs -rm -R UERCountiesCount.out
hfs -rm -R UERAlbanyCounty.out


head UERCountiesCount.out
head UERAlbanyCounty.out



'''
