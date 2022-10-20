from locust import HttpUser, task, run_single_user


class Hello(HttpUser):
    
    @task
    def hello_world(self):
        self.client.post("/api/conversations/4913/read?token=REVWMDAwMTowZG41VW9admZoZFAzejVCV3RzTGw3YkNacVoy")
        self.client.post("/api/conversations/4913/read?sizeinfo=DEV0001")
        # self.client.get("/api/shops?token=REVWMDAwMTowZG41VW9admZoZFAzejVCV3RzTGw3YkNacVoy")
        # self.client.get("/api/contacts?token=REVWMDAwMTowZG41VW9admZoZFAzejVCV3RzTGw3YkNacVoy")
        # self.client.get("/api/vehicles?token=REVWMDAwMTowZG41VW9admZoZFAzejVCV3RzTGw3YkNacVoy")
        
        # self.client.get("/")
        # self.client.get("/")get