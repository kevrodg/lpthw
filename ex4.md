##ex4 study drill##

Explain the Traceback error:

	Traceback (most recent call last):
	File "ex4.py", line 8, in <module>
	average_passengers_per_car = car_pool_capacity / passenger
	NameError: name 'car_pool_capacity' is not defined”

	(Excerpt From: Zed A. Shaw. “Learn Python the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code, Third Edition (Zed Shaw's Library).” iBooks.)
	
On line 8 of ex4.py, the `car_pool_capacity` variable was not defined. Most likely, it was spelled `carpool_capacity` instead of `car_pool_capacity` (note the extra underscore in the latter).