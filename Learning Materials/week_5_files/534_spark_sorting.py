# 5.3.4 Sorting using Spark
# In this example, you will see how besides performing word count, we can also sort by the frequency of the words extracted from the text file text.txt.
# Can you think of other processes you may use Spark to perform?

import sys
from typing import Tuple

from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName("PythonSort")\
    .getOrCreate()

lines = spark.read.text("text.txt").rdd.map(lambda r: r[0])

sortedCount = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1])

output = sortedCount.collect()
for (word, wordcount) in output:
    print(word, wordcount)

spark.stop()