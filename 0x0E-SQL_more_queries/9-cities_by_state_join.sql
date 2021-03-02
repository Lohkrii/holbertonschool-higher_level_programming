-- Lists all cities contained in the hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id=cities.state_id;
