import os
import pytest
from PIL import Image

import api.credits as credits
import faker

fake = faker.Faker()


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        if self.authorize:
            self.api_client.post_login(credits.email, credits.password)

    def get_image_id(self):
        response = self.api_client.post_upload_image(self.get_random_picture())
        assert response.status_code == 200
        return response.json()['id']

    def get_url_id(self):
        response = self.api_client.get_url_id(fake.url())
        assert response.status_code == 200
        return response.json()['id']

    def create_campaign(self):
        url_id = self.get_url_id()
        image_id = self.get_image_id()
        name = fake.word()
        response = self.api_client.post_create_campaign(name=name, image_id=image_id, url_id=url_id)
        assert response.status_code == 200
        campaign_id = response.json()['id']
        campaign_status = self.api_client.get_campaign_status(campaign_id)
        return campaign_id, campaign_status

    def get_random_picture(self):
        color = tuple(map(int, fake.rgb_color().split(',')))
        size = (240, 400)
        img = Image.new('RGB', size, color)
        img_name = f'{fake.color_name()}.png'
        path = os.path.abspath(f'../api_homework/files/{img_name}')
        img.save(path)
        return path

    def create_segment(self):
        name = fake.first_name()
        response = self.api_client.post_create_segment(name=name, pass_condition=1, object_type='remarketing_player')
        assert response.status_code == 200
        return response.json()['id']

    def delete_segment(self, segment_id):
        response = self.api_client.post_delete_segment(segment_id=segment_id)
        assert response.status_code == 200
        return response.json()['successes'][0]['source_id']
