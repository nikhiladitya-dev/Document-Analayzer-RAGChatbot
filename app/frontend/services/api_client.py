import requests

from utils.constants import API_URL


class APIClient:

    BASE_URL = API_URL

    def process_document(
        self,
        uploaded_file,
    ):

        response = requests.post(
            f"{self.BASE_URL}/upload-document",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type,
                )
            },
        )

        response.raise_for_status()

        return response.json()

    def chat(
        self,
        question: str,
    ):

        response = requests.post(
            f"{self.BASE_URL}/chat",
            json={
                "question": question,
            },
        )

        response.raise_for_status()

        return response.json()

    def health(
        self,
    ):

        response = requests.get(
            f"{self.BASE_URL}/health"
        )

        response.raise_for_status()

        return response.json()