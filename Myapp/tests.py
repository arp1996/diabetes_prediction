from django.test import TestCase


class PredictionViewTests(TestCase):
    def test_prediction_page_returns_success(self):
        response = self.client.post(
            "/result",
            {
                "RestingBP": "140",
                "Cholesterol": "289",
                "FastingBS": "0",
                "MaxHR": "172",
                "Oldpeak": "0",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Prediction is")
