# Total Sales per Store

Sample task given in [Intro to Hadoop and MapReduce](www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) course on Udacity

### Data set (tab delimited)
Can be found [Here](https://drive.google.com/open?id=13AobBZtgLhz5dDsvR88-EVgvcxyDXfFp)
* Date
* Time
* Store-Name
* Product-Type
* Cost
* Method

### Key: value chosen for MapReduce

* Store-Name: Cost

### Usage 

#### Test Locally
1. Download the data set and move it to this folder
2. Run the following command
    
    For Windows (PowerShell):
    ```cmd
    > gc -TotalCount 50 data.txt | python mapper.py | sort | python reducer.py
    ```
    -TotalCount n (sets the no of lines to read from the file mentioned)
    
    For Linux :
    ```bash
    $ head -n 50 data.txt | python3 mapper.py | sort | python3 reducer.py
    ```
    
#### Run on a Hadoop cluster
1. Download the data set and move it to this folder
2. Start hadoop cluster (Instructions in the project README.md file)
3. Create the input directory

    For Windows (PowerShell) and Linux:
    ```
    > hadoop fs -mkdir /input_dir
    ```
4. Upload the data set to input directory in Hadoop DFS 

    For Windows (PowerShell) and Linux:
    ```
    > hadoop fs -put <local-input-data-path> <hdfs-input-data-path>
    ```
    
    eg. 
    ```
    > hadoop fs -put P:\PyCharmProjects\mapreduce-jobs-for-hadoop\total-sales-per-store\hadoop-streaming-python\data.txt /input_dir/data.txt
    ```
5. Run

    For Windows (PowerShell) and Linux:
    ```
     > hadoop jar <local-absolute-path-to-hadoop-streaming-jar-file> \
     -input <hdfs input dir location> \
     -output <hdfs input dir location> \
     -mapper <command-for-running-mapper.py> \
     -reducer <command-for-running-reducer.py> \
     -file <relative-path-to-mapper.py> \
     -file <relative-path-to-reducer.py>
    ```
    
    eg. For Windows
    ```
    > hadoop jar C:\Hadoop-2.8.4\share\hadoop\tools\lib\hadoop-streaming-2.8.4.jar `
     -input /input_dir `
     -output /output_dir `
     -mapper "python mapper.py" `
     -reducer "python reducer.py" `
     -file mapper.py `
     -file reducer.py
    ```
    
    eg. For Linux
    ```
    > hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.4.jar \
     -input /input_dir \
     -output /output_dir \
     -mapper "python3 mapper.py" \
     -reducer "python3 reducer.py" \
     -file mapper.py \
     -file reducer.py
    ```
6. Output is stored in `part-00000` file in `output_dir` on the Hadoop DFS
    
    For Windows(PowerShell) and Linux:
    ```
    > hadoop fs -cat /output_dir/part-00000
    ``` 

     