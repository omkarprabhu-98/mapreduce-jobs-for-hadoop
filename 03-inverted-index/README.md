# Total Sales per Store

Task given in [Intro to Hadoop and MapReduce](www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) course on Udacity

### Data set (tab delimited)
Can be found [Here](https://drive.google.com/open?id=1PFotAebSMf0ltFihIymom1vZkBzcsk00)

Contains various field related to forum posts
* id
* title
* tagnames
* author_id
* body
* node_type
* parent_id	
... 

### Key: value chosen for MapReduce

#### Intermediate
* word: node_id

#### Final
* word: list of node_id's

### Usage 

Each folder contains the implementation details and instructions