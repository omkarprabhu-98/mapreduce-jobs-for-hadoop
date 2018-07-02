### Usage 

#### Test Locally
1. Download the data set and move it to this folder
2. Run the following command
    
    For Windows (PowerShell):
    ```cmd
    > gc -TotalCount 10000 .\forum_node.tsv, .\forum_users.tsv | python .\mapper.py | sort | python .\reducer.py | Select-String -Pattern '100066904'
    ```
    -TotalCount n (sets the no of lines to read from the file mentioned)
    - Select-String searches for the string pattern in the piped output
    
    For Linux :
    ```bash
    $ head -n 10000 forum_node.tsv forum_users.tsv | python3 mapper.py | sort | python3 reducer.py | grep '100066904'
    ```
    
    This command should yield the following output:
    ```
    {'user_id': '"100066904"', 'id': '"4001273"', 'title': '""', 'tagnames': '"technical-support "', 'node_type': '"comment"', 'parent_id': '"4001270"', 'abs_parent_id': '"4001269"', 'added_at': '"2012-08-04
    13:03:12.458256+00"', 'score': '"0"\n', 'reputation': '"3845"', 'gold': '"0"', 'silver': '"1"', 'bronze': '"8"\n'}
    {'user_id': '"100066904"', 'id': '"9004946"', 'title': '""', 'tagnames': '"ph100 "', 'node_type': '"answer"', 'parent_id': '"9004941"', 'abs_parent_id': '"9004941"', 'added_at': '"2012-07-17 21:33:37.815283+00"', 'score':
    '"4"\n', 'reputation': '"3845"', 'gold': '"0"', 'silver': '"1"', 'bronze': '"8"\n'}
    {'user_id': '"100066904"', 'id': '"9006952"', 'title': '""', 'tagnames': '"ph100 "', 'node_type': '"comment"', 'parent_id': '"9006917"', 'abs_parent_id': '"9005710"', 'added_at': '"2012-08-03 19:40:07.717837+00"', 'score':
    '"0"\n', 'reputation': '"3845"', 'gold': '"0"', 'silver': '"1"', 'bronze': '"8"\n'}
    {'user_id': '"100066904"', 'id': '"9006957"', 'title': '""', 'tagnames': '"ph100 "', 'node_type': '"comment"', 'parent_id': '"9006946"', 'abs_parent_id': '"9006925"', 'added_at': '"2012-08-03 20:26:51.344232+00"', 'score':
    '"0"\n', 'reputation': '"3845"', 'gold': '"0"', 'silver': '"1"', 'bronze': '"8"\n'}
    {'user_id': '"100066904"', 'id': '"9007120"', 'title': '""', 'tagnames': '"ph100 "', 'node_type': '"comment"', 'parent_id': '"9007087"', 'abs_parent_id': '"9006308"', 'added_at': '"2012-08-05 20:23:53.012493+00"', 'score':
    '"0"\n', 'reputation': '"3845"', 'gold': '"0"', 'silver': '"1"', 'bronze': '"8"\n'}

    ```
    
#### Run on a Hadoop cluster
1. Download the data set and move it to this folder
2. Start hadoop cluster (Instructions in the project README.md file)
3. Create the input directory

    For Windows (PowerShell) and Linux:
    ```
    > hadoop fs -mkdir /input_dir
    ```
4. Upload the data sets to input directory in Hadoop DFS 

    For Windows (PowerShell) and Linux:
    ```
    > hadoop fs -put <local-input-data-path> <hdfs-input-data-path>
    ```
    
    eg. 
    ```
    > hadoop fs -put P:\PyCharmProjects\mapreduce-jobs-for-hadoop\04-combine-datasets\hadoop-streaming-python\forum_node.tsv /input_dir/data.tsv
    > hadoop fs -put P:\PyCharmProjects\mapreduce-jobs-for-hadoop\04-combine-datasets\hadoop-streaming-python\forum_users.tsv /input_dir/data1.tsv
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

     