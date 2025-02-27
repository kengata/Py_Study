LOAD DATA INFILE '/home/ec2-user/Py_study/meigara_m.csv' 
INTO TABLE meigara_m 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;
