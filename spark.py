from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaIntegration") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1") \
    .getOrCreate()


df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "your_topic_name") \
    .load()


query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
    
