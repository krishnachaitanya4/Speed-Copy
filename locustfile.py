from locust import HttpUser,TaskSet,task
'''
class LoadTest(TaskSet):
    @task
    def home_get(self):
        response = self.client.get('/')
        self.csrftoken = response.cookies['csrftoken']
        self.headers = {'X-CSRFToken': self.csrftoken}

class WebsiteUser(HttpUser):
    tasks = [LoadTest]
'''

class FirstTest(HttpUser):
    @task(1)
    def hello_world(self):
        self.client.get("")
