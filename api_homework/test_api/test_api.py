import pytest
import faker
from .base import ApiBase

fake = faker.Faker()


class TestApi(ApiBase):
    @pytest.mark.API('API')
    def test_create_company(self):
        url_id = self.api_client.get_url_id(fake.url())
        file = self.path_to_image
        image_id = self.api_client.post_upload_image(file)
        name = fake.company()
        campaign_id = self.api_client.post_create_campaign(name, image_id=image_id, url_id=url_id)
        campaign_status = self.api_client.get_campaign_status(campaign_id)
        assert campaign_status == "NO_ALLOWED_BANNERS"
        self.api_client.delete_campaign(campaign_id)

    @pytest.mark.API('API')
    def test_create_segment(self):
        name = fake.first_name()
        segment_id = self.api_client.post_create_segment(name=name, pass_condition=1, object_type='remarketing_player')
        segment_status_code = self.api_client.get_segment_status_code(segment_id)
        assert segment_status_code == 200

    @pytest.mark.API('API')
    def test_delete_segment(self):
        name = fake.first_name()
        segment_id = self.api_client.post_create_segment(name=name, pass_condition=1, object_type='remarketing_player')
        delete_segment_id = self.api_client.post_delete_segment(segment_id)
        segment_status_code = self.api_client.get_segment_status_code(delete_segment_id)
        assert segment_status_code == 404
