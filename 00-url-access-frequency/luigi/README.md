### Usage 
1. Download the data set and move it to this folder
2. Start hadoop cluster (Instructions in the project README.md file)
3. Create the input directory

    Linux:
    ```
    $ hadoop fs -mkdir /input_dir
    ```
4. Upload the data set to input directory in Hadoop DFS 

    Linux:
    ```
    $ hadoop fs -put <local-input-data-path> <hdfs-input-data-path>
    ```
    
    eg. 
    ```
    $ hadoop fs -put data.txt /input_dir/data.txt
    ```
5. Run the following command:
    
    ```
    $ PYTHONPATH='' luigi --module <python_file_name> <task_name> --local-scheduler 
    ```   
    
    eg.     
    ```
    $ PYTHONPATH='' luigi --module url_access_frequency UrlAccessFrequency --local-scheduler
    ```
6. Output should be in the `part-*` files in `output_dir_luigi/out` directory in HDFS
    
    Run the following to check files
    ```
    $ hadoop fs -ls /output_dir_luigi/out/
    ``` 
    
    Check contents of one file 
    ```
    $ hadoop fs -cat /output_dir_luigi/out/part-00000
    ```