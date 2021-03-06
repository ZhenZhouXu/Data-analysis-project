import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()
data2020 = sc.textFile(sys.argv[1], 1).mapPartitions(lambda x: reader(x))
datapast = sc.textFile(sys.argv[2], 1).mapPartitions(lambda x: reader(x))

data2020 = data2020.filter(lambda x: "OCCUR" not in x).map(lambda x: (x[1], 1))
datapast = datapast.filter(lambda x: "OCCUR" not in x).map(lambda x: (x[1], 1))

result2020 = data2020.reduceByKey(lambda x, y: x + y).sortBy(lambda x: (x[0][6:], x[0][:2], x[0][3:5]))
resultpast = datapast.reduceByKey(lambda x, y: x + y).sortBy(lambda x: (x[0][6:], x[0][:2], x[0][3:5]))

output2020 = result2020.map(lambda x: x[0] + ',' + str(x[1]))
resultpast = resultpast.map(lambda x: x[0] + ',' + str(x[1]))

output2020.saveAsTextFile("ShootingCount2020.out")
resultpast.saveAsTextFile("ShootingCountPast.out")



'''
module load python/gnu/3.6.5
module load spark/2.4.0

rm -rf ShootingCount2020.out
rm -rf ShootingCountPast.out

hfs -rm -R ShootingCount2020.out
hfs -rm -R ShootingCountPast.out

spark-submit --conf \
spark.pyspark.python=/share/apps/python/3.6.5/bin/python \
ShootingCount.py NYPD_Shooting_Incident_Data__Year_To_Date_.csv \
NYPD_Shooting_Incident_Data__Historic_.csv

hfs -getmerge ShootingCount2020.out ShootingCount2020.out
hfs -getmerge ShootingCountPast.out ShootingCountPast.out

hfs -rm -R ShootingCount2020.out
hfs -rm -R ShootingCountPast.out

head ShootingCount2020.out
head ShootingCountPast.out

'''
