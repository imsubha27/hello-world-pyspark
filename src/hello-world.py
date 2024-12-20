# src/hello_world.py

from pyspark.sql import SparkSession

def main():
    # Initialize SparkSession
    spark = SparkSession.builder \
    .appName("HelloWorld") \
    .getOrCreate()
    
    # Print "Hello, World!"
    print("Hello, World!")
    
    # Create a simple DataFrame
    data = [(1, "Anirban", 25), (2, "Subhajit", 24), (3, "Subhankar", 23)]
    columns = ["ID", "Name", "Age"]
    df = spark.createDataFrame(data, columns)
    
    # Show the DataFrame
    df.show()
    
    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()