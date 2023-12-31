CREATE TABLE location_table (
  latitude VARCHAR(255),
  longitude VARCHAR(255),
  timestamp DOUBLE,
  message VARCHAR(50),
  traceback VARCHAR(100)
);

CREATE TABLE speed_table (
  latitude VARCHAR(255),
  longitude VARCHAR(255),
  timestamp DOUBLE,
  message VARCHAR(50),
  traceback VARCHAR(100),
  iss_speed DOUBLE,
  iss_distance DOUBLE,
  iss_time_elapsed DOUBLE
);

CREATE TABLE acc_table (
  latitude VARCHAR(255),
  longitude VARCHAR(255),
  timestamp DOUBLE,
  message VARCHAR(50),
  traceback VARCHAR(100),
  iss_acceleration DOUBLE,
  iss_semi_major_axis DOUBLE
);


select * from loaction_table;


select * from speed_table;

select * from acc_table;


select min(iss_speed),max(iss_speed) from speed_table;

select min(iss_distance) from speed_table;
