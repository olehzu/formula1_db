use formula1_db;

############################################
## selects all drivers of German nationality
## Works
############################################
select forename, surname, dob as birthdate
from drivers
where nationality = "German"
order by surname;

########################################################
## selects driver info of winners and their fastest laps
## Works
########################################################
select forename, surname, name, year, fastestLapTime
from drivers
inner join results
on drivers.driverId = results.driverId
inner join races
on results.raceId = races.raceId
where position=1;

############################################
## selects constructors that finished fourth
## Works
############################################
select name
from constructors
where constructorId in (
	select constructorId
    from constructorStandings
    where position = 4);
    
#######################################################################
## selects races and the fastest stops if they are less than 23 seconds
## Works
#######################################################################
select name, year, pits.fastestStop from races
inner join (
	SELECT raceId, MIN(duration) as fastestStop
	FROM pitStops 
	WHERE duration < 23.0
	group by raceId
) pits
on races.raceId = pits.raceId;

################################
## Inserts a new driver (myself)
## Works
################################
insert ignore into drivers
value (6767, "zubariev", 67, "ZUB", "Oleh", "Zubariev", '2006-05-19', "Ukrainian", "https://www.linkedin.com/in/oleh-zubariev/");

select * from drivers where driverId=6767;


##################################################
## deletes all constructors of russian nationality
## Works
##################################################
select * from constructors where nationality = "Russian";

delete ignore from constructors 
where constructorId>0 and nationality = "Russian";

select * from constructors where nationality = "Russian";


################################################################################################################
## results has a foreign key constructorId with on delete set null constraint.
## to test it we select certain rows from results based on the foreign key,
## then delete that constructor from the parent table and check if those rows of the child table are set to null
## Works
################################################################################################################
select * from results where constructorId = 6 and grid = 22; 

delete ignore from constructors
where constructorId = 6;

select * from results where constructorId = 6 and grid = 22;


############################################################################################################
## constructorStandings has a foreign key constructorId with on update cascade constraint.
## to test it we select certain rows from constructorStandings based on the foreign key,
## then update that constructor from the parent table and check if those rows of the child table are updated
## Works
############################################################################################################
select * from constructorStandings where constructorId=9;

update constructors
set constructorId=670
where constructorId=9;

select * from constructorStandings where constructorId=670;

