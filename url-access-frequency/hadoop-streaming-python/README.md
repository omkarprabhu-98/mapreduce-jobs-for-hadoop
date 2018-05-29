#URL Access Frequency 

### Data set (Apache log from http://www.almhuette-raith.at/apache-log/access.log)
Can be found [Here](https://drive.google.com/open?id=1pOZBMfIGk6ok5d4R65ORsYQRVX0CuqS1)

### Key: value chosen for MapReduce

* URL: 1

### Usage 

#### Test Locally
1. Download the data set and move it to this folder
2. Run the following command
    
    For Windows (PowerShell):
    ```cmd
    > gc -TotalCount 50 data.txt | python mapper.py | sort | python reducer.py
    ```
    -TotalCount n (sets the no of lines to read from the file mentioned)
    
#### Run on a Hadoop cluster
1. Download the data set and move it to this folder
2. Start hadoop cluster (Instructions in the project README.md file)
3. Upload the data set to Hadoop DFS

    For Windows (PowerShell):
    ```
    > hadoop fs -put <local-input-data-path> <hdfs-input-data-path>
    ```
    
    eg. 
    ```
    > hadoop fs -put P:\PyCharmProjects\mapreduce-jobs-for-hadoop\url-access-frequency\hadoop-streaming-python\data.txt /input_dir/data.txt
    ```
4. Run

    For Windows (PowerShell):
    ```
     > hadoop jar <local-absolute-path-to-hadoop-streaming-jar-file> \
     -input <hdfs input dir location> \
     -output <hdfs input dir location> \
     -mapper <command-for-running-mapper.py> \
     -reducer <command-for-running-reducer.py> \
     -file <relative-path-to-mapper.py> \
     -file <relative-path-to-reducer.py>
    ```
    
    eg.
    ```
    > hadoop jar C:/Hadoop-2.8.4/share/hadoop/hadoop-streaming-2.8.4.jar \
     -input /input_dir \
     -output /output_dir \
     -mapper "python mapper.py" \
     -reducer "python reducer.py" \
     -file mapper.py \
     -file reducer.py
    ```
6. Output is stored in `part-00000` file in `output_dir` on the Hadoop DFS
    
    For Windows(PowerShell):
    ```
    > hadoop fs -cat /output_dir/part-00000
    ``` 

     