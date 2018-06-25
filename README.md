# MapReduce Jobs for Hadoop

Contains a collection of example of jobs in python for Hadoop using the MapReduce programming model

### Installation 

1. Hadoop
    
    #### For Windows 10:
    
    Follow [this](https://github.com/MuhammadBilalYar/Hadoop-On-Window) for initial setup 
    
    Follow [this](http://www.informit.com/articles/article.aspx?p=2190194&seqNum=2) for configurations for hadoop single node yarn cluster

    #### For Ubuntu:
    
    ##### For Stand-Alone mode 
    
    Follow [this](https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-16-04) 
    
    ##### For Pseudo Distributed Mode:
    
    Follow [this](http://www.bogotobogo.com/Hadoop/BigData_hadoop_Install_on_ubuntu_16_04_single_node_cluster.php) for initial setup and installation
    
    Follow [this](http://www.informit.com/articles/article.aspx?p=2190194&seqNum=2) for configurations for hadoop single node yarn cluster 

    #### Configuration files used can be found [here](https://drive.google.com/open?id=1Wa0tmdg0IrwdlnOz7EyTRXgTY65qqugL)

2. Install Python (Used Python 3.6 in my virtual environment) and pip (Used latest version for python3)

3. Luigi 
    
    Used Python 2.7.15 for Ubuntu with luigi 2.7.5.  
    
    Run the command 
    ```
    pip install luigi
    ```
    
    Errors:
    
    1. Windows 10: Problem when running luigi [View here](https://github.com/spotify/luigi/issues/2218)   
    2. Python 3.6 on Ubuntu: mechanizer module not available only for python 2.x versions
    
