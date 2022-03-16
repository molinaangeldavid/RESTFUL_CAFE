# **Cafe memo**

## An Api that you input the features of a Cafe that you've been there.

---

**REQUEST**

## GET 

- /all 
> List all the features of all the Cafes available in the db. 

- /random
> List a random Cafe and its features.

- /search
> Search a specific location and show the first Cafe that be equal to the location requested.

## **POST**: 

- /add
> Create a new Cafe with all the features the cafe has. 

## **PATCH**
- /update-price/id
> Update the price coffee that matches the id requested.

## **DELETE**
- /reported_closed/id
> Delete the Cafe which id matches with the requested
*NEED A API KEY TO HAVE THE PERMISSION TO DELETE THE CAFE*

**CREATE A CAFE**

### You need the following data to add another Cafe:

1. *cafe_name* as the name of the Cafe.
2. *map_url* as the url where the Cafe is.
3. *img_url* as the url where you can look the outside/inside appearance of the Cafe.
4. *seats* as the quantity of seats that the Cafe has. 
5. *has_toilet* (Boolean value) if the Cafe has or not a toilet.
6. *has_wifi* (Boolean value) if the Cafe has or not WiFi internet.
7. *has_sockets* (Boolean value) if the Cafe has sockets to connect something.
8. *can_take_calls* (Boolean value) if the Cafe has any phone that you can take calls free or not.
9. *coffee_price* as the price of the general coffee. 
