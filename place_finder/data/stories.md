## greet
* greet
    - utter_greet
	

## thanks
* thanks
    - utter_thanks
			
	
## goodbye
* goodbye
    - utter_goodbye
	
## location_search_01
* greet
	- utter_greet
* place_search{"query":"restaurant", "number":"55"}
	- action_place_search
	- slot{"location_match":"one"}
	- slot{"rating":"4.5"}
	- slot{"address":"Alexanderplatz 15"}
	- slot{"opening_hours":"open"}
* address
	- utter_address
* rating
	- utter_rating
* opening_hours
	- utter_opening_hours
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye
	
	
## location_search_02
* greet
	- utter_greet
* place_search{"query":"restaurant", "number":"21"}
	- action_place_search
	- slot{"location_match":"none"}
	- utter_no_results
* goodbye
	- utter_goodbye	
	
	
	
## location_search_03
* greet
	- utter_greet
* place_search{"query":"restaurant", "number":"36"}
	- action_place_search
	- slot{"location_match":"one"}
	- slot{"rating":"4.7"}
	- slot{"address":"Marylebone 15"}
	- slot{"opening_hours":"closed"}
* address
	- utter_address
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	
	
## location_search_04
* greet
	- utter_greet
* place_search{"query":"restaurant", "number":"25"}
	- action_place_search
	- slot{"location_match":"one"}
	- slot{"rating":"3.0"}
	- slot{"address":"Bridge Street 175"}
	- slot{"opening_hours":"open"}
* rating
	- utter_rating	
* address
	- utter_address
* opening_hours
	- utter_opening_hours
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	
	
	
## location_search_05
* greet
	- utter_greet
* place_search{"query":"restaurant", "number":"95"}
	- action_place_search
	- slot{"location_match":"one"}
	- slot{"rating":"4.7"}
	- slot{"address":"King's street"}
	- slot{"opening_hours":"closed"}
* opening_hours
	- utter_opening_hours	
* address
	- utter_address
* rating
	- utter_rating	
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	
	
		
	
	
## location_search_07
* greet
	- utter_greet
* place_search{"query":"restaurant"}
	- utter_what_radius
* inform{"number":"200"}
	- action_place_search
	- slot{"location_match":"one"}
	- slot{"rating":"4.2"}
	- slot{"address":"Alexanderplatz 26"}
	- slot{"opening_hours":"closed"}
* address
	- utter_address
* rating
	- utter_rating
* opening_hours
	- utter_opening_hours
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye		

	
	
## location_search_08
* greet
	- utter_greet
* place_search{"query":"restaurant"}
	- utter_what_radius
* inform{"number":"275"}
	- action_place_search
	- slot{"location_match":"none"}
	- utter_no_results
* goodbye
	- utter_goodbye	

	
## location_search_09
* greet
	- utter_greet
* place_search{"query":"restaurant"}
	- utter_what_radius
* inform{"number":"250"}
	- action_place_search
	- slot{"location_match":"one"}
	- slot{"rating":"2.2"}
	- slot{"address":"London Bridge"}
	- slot{"opening_hours":"open"}
* address
	- utter_address
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	
	
	
	
## location_search_10
* greet
	- utter_greet
* place_search{"query":"restaurant"}
	- utter_what_radius
* inform{"number":"200"}
	- action_place_search
	- slot{"location_match":"one"}
	- slot{"rating":"5.2"}
	- slot{"address":"London 273"}
	- slot{"opening_hours":"closed"}
* opening_hours
	- utter_opening_hours
* address
	- utter_address
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	


