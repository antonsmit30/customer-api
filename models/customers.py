# Create our Customer Model
# The customer Model will do the backend work (customer resource for front end requests)

#In memory DB
customers = []

class customerModel():

    #Init our customer
    def __init__(self, name, devices, probe):
        self.name = name
        self.probe = probe
        self.devices = devices

        # adding temp dict for now
        self.tempdict = {'name': self.name, 'probe': self.probe, 'devices': self.devices}


    def json(self):
        return {'name': self.name, 'probe': self.probe, 'devices': self.devices}

    # We will point this to DB later
    @classmethod
    def find_by_name(cls, name):
        print(customers)
        for item in customers:
            print(item)
            if item["name"] == name:
                return item



    # Save to DB
    # We will work on this later. for now just push to a list.
    def save_to_db(self):
        customers.append(self.tempdict)

    # Delete from DB
    # We will work on this later. for now just delete from list







