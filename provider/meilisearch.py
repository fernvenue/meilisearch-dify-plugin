from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from typing import Any

import requests

class MeilisearchDifyPluginProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            response = requests.get(
                # credentials["base_url"] + "/version",
                # Here we don't use version API because our API key may not have access to it, and we just need to make sure meilisearch API works;
                credentials["base_url"],
                headers={"Authorization": f"Bearer {credentials['meilisearch_api_key']}"}
            )
            if response.json().get("status") != "Meilisearch is running":
                raise ToolProviderCredentialValidationError(
                    f"Meilisearch API is not reachable. Response: {response.json()}"
                )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
