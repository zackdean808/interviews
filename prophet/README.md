[200~"""
Sports evernt are provided by data providers, and Prophet ingest the data and them display them on our site. Assuming that we get such events from CSV strings, and each one of them have following values, for example 

"tournament_name, competitor_1, completitor_2, start_time, city, state \n
 t_1, c_1, c_2, 1659900000, city_1, state_1 \n
 t_1, c_1, c_3, 1659920000, city_2, state_1 \n
 t_1, c_2, c_4, 1660020000, city_2, state_1 \n
 t_2, c_3, c_5, 1659900000, city_1, state_1 \n
 t_3, c_2, c_3, 1659920000, city_1, state_2 \n
 t_2, c_2, c_4, 1670020000, city_2, state_1 \n
"
Ingest above strings, return result for following quesitons:
1. return all games happened in city_1 and state_1
2. return all games starts after 1659900001

"""
