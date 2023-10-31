"""
Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

{
"bookingid": 2384,
"booking": {
"firstname": "PRAMOD",
"lastname": "Dutta",
"totalprice": 432,
"depositpaid": False,
"bookingdates": {
"checkin": "2022-01-01",
"checkout": "2022-01-01"
},
"additionalneeds": "Lunch"
}
}
"""
json_response_Dict= {
"bookingid": 2384,
"booking": {
"firstname": "PRAMOD",
"lastname": "Dutta",
"totalprice": 432,
"depositpaid": False,
"bookingdates": {
"checkin": "2022-01-01",
"checkout": "2022-01-02"
},
"additionalneeds": "Lunch"
}
}

print("json_response_Dict:",json_response_Dict)
print(type(json_response_Dict))
print("Booking ID:",json_response_Dict["bookingid"])
print("checkin date:",json_response_Dict["booking"]["bookingdates"]["checkin"])
print("checkout date:",json_response_Dict["booking"]["bookingdates"]["checkout"])