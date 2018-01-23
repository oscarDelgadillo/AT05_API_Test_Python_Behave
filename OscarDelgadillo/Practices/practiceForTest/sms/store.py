# Create a new class, SMS_store. The class will instantiate SMS_store objects,
# similar to an inbox or outbox on a cellphone:
# 	my_inbox = SMS_store()
# This store can hold multiple SMS messages (i.e. its internal state will just be a list of messages).
# Each message will be represented as a tuple:
# 	(has_been_viewed, from_number, time_arrived, text_of_SMS)
# The inbox object should provide these methods:
# 	my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
# 		# Makes new SMS tuple, inserts it after other messages
#         # in the store. When creating this message, its # has_been_viewed status is set False.
# 	my_inbox.message_count()
#  		# Returns the number of sms messages in my_inbox
# 	my_inbox.get_unread_indexes()
# 		# Returns list of indexes of all not-yet-viewed SMS messages
# 	my_inbox.get_message(i)
# 		# Return (from_number, time_arrived, text_of_sms) for message[i]
# 		# Also change its state to "has been viewed".
# 	 	# If there is no message at position i, return None
# 	my_inbox.delete(i) # Delete the message at index i
#   my_inbox.clear()  Delete all messages from inbox
#
# Write the class, create a message store object, write tests for these methods, and implement the methods.

from practiceForTest.sms.sms import SMS


class SMS_store:
    def __init__(self):
        self.list_SMS = []

    def add_new_arrival(self, number, time, message):
        sms = SMS(number, time, message)
        self.list_SMS.append(sms)

    def message_count(self):
        return len(self.list_SMS)

    def get_unread_indexes(self):
        list_unread = []
        index = 0
        while index < len(self.list_SMS):
            if not self.list_SMS[index].get_has_been_viewed():
                list_unread.append(index)
            index += 1
        return list_unread

    def get_message(self, index):
        try:
            self.list_SMS[index].get_SMS()
            self.list_SMS[index].set_has_been_viewed(True)
        except IndexError:
            return None

    def delete(self, index):
        try:
            self.list_SMS.pop(index)
        except IndexError:
            return None

    def clear(self):
        self.list_SMS.clear()

    def read_sms(self):
        for msg in self.list_SMS:
            print(msg.get_SMS())
