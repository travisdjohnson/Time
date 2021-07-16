import datetime
CA = datetime.date (2001, 6, 3) #The day I moved to California the first time
GA = datetime.date (2005, 9, 20) #The day I moved back to Georgia
NY = datetime.date(2013, 8, 25) #The day I moved to New York
CA2= datetime.date(2017, 7, 7) #The day I moved to California the second time
duration = (GA - CA)
duration2= (CA2 - NY)
today = datetime.date.today()
time_elapsed = (today - CA2)
message = "The first time I moved to California was on {:%A, %B %d, %Y}."
message1 = "I moved back to Georgia on {:%A, %B %d, %Y}."
message2 = "I moved to New York on {:%A, %B %d, %Y}."
message3 = "I moved back to California on {:%A, %B %d, %Y}."
message4 = "I lived in California the first time for {}."
message5 = "I lived in New York for {}."
message6 = "I have been back in California {}."
print(message.format(CA))
print(message1.format(GA))
print(message2.format(NY))
print(message3.format(CA2))
print(message4.format(duration))
print(message5.format(duration2))
print(message6.format(time_elapsed))
