from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName('Firstprogram').getOrCreate()

text_file = spark.read.text("text.txt").rdd.map(lambda r: r[0])

counts = text_file.flatMap(lambda line: line.split(" ")) \
                            .map(lambda word: (word, 1)) \
                           .reduceByKey(lambda x, y: x + y)
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))