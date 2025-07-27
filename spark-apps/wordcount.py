from pyspark import SparkConf, SparkContext
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: test.py <input-file-path>")
        sys.exit(-1)

    input_path = sys.argv[1]
    print(f"Reading from: {input_path}")

    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)

    # Read file lines
    lines = sc.textFile(input_path)

    # Word count logic
    word_counts = (
        lines
        .flatMap(lambda line: line.split())       # Split each line into words
        .map(lambda word: (word.lower(), 1))      # Create (word, 1) pairs, lowercase for consistency
        .reduceByKey(lambda a, b: a + b)          # Sum counts for each word
    )

    # Collect and print results
    for word, count in word_counts.collect():
        print(f"{word}: {count}")

    sc.stop()

if __name__ == "__main__":
    main()
