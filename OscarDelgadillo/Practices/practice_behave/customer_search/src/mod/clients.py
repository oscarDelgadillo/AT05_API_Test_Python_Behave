class Clients:
    def __init__(self):
        self.list_clients = {}
        self.set_list_clients()

    def get_list_clients(self):
        return self.list_clients

    def set_list_clients(self):
        self.list_clients.update({"ID001": "Homero Simpson"})
        self.list_clients.update({"ID002": "March Simpson"})
        self.list_clients.update({"ID003": "Bart Simpson"})
        self.list_clients.update({"ID004": "Lisa Simpson"})

    def get_name_by_id(self, id):
        return self.list_clients.get(id)

    def get_id_by_name(self, name):
        for client in self.list_clients:
            if self.list_clients[client] == name:
                return client

    def exist_client_in_list(self, name):
        for client in self.list_clients:
            if self.list_clients[client] == name:
                return True
        return False
