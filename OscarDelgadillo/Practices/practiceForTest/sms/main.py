from datetime import datetime
from practiceForTest.sms.store import SMS_store

sms = SMS_store()

# insert new message and added to list
sms.add_new_arrival(72212345, datetime.now().strftime('[%x-%X]'), "hi world.")
sms.add_new_arrival(72245678, datetime.now().strftime('[%x-%X]'), "this is a test")
sms.add_new_arrival(72245885, datetime.now().strftime('[%x-%X]'), "this is an other message")

# count quantity of messages
print('Quantity of messages: ', sms.message_count())

# return number of index of messages not reading
print("Messages not reading (only index): ", sms.get_unread_indexes())

# given a index display message
sms.get_message(1)
sms.get_message(10)
print("Messages not reading (only index): ", sms.get_unread_indexes())

# given a index delete a message
sms.delete(0)
print('Quantity of messages: ', sms.message_count())

# errase all message stored
sms.clear()
print('Quantity of messages: ', sms.message_count())
