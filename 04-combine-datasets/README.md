# Combine Data sets

Task given in [Intro to Hadoop and MapReduce](www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) course on Udacity

Involves rating each post in the forum based on the reputation. Thus the two data sets mentioned
below have to be combined

### Data set (tab delimited)
Two data sets can be found [Here](https://drive.google.com/open?id=1-mWTG4qwVLA8fhILmCtg0BbdMM_OZPx3)

1. Contains various field related to forum posts
    * id
    * title
    * tagnames
    * author_id
    * body
    * node_type
    * parent_id	
    ... 

2. Contains information related to forum users
    * user id
    * reputation
    * gold
    * silver
    * bronze

### MapReduce 

Combine the data sets with common key as author id

* Mapper 
    
    Split and required fields from each line from the two data sets 
    
    Keep field with user id first to help in shuffle and sort

* Shuffle Sort
    
    Plays an important role here 
    
    For each user in a sorted order,
    
    It will produce the line with user data first,
    
    Then the lines with forum node data containing the same user id

* Reducer
    
    So after shuffle and sort the reducer(s) will get data for user_id as a key
    (as data for each key will land on a particular reducer)
    
    Thus it will first take a line for user data and store its fields in a row variable of the new data set
     
    Then for each following line, it will take fill the rest of the data required for the row to complete and print out this row
    

### Usage 

Each folder contains the implementation details and instructions