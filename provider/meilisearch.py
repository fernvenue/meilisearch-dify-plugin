from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from typing import Any

import meilisearch

class MeilisearchDifyPluginProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            client = meilisearch.Client(credentials["base_url"], credentials["meilisearch_api_key"])
            client.get_version()
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
