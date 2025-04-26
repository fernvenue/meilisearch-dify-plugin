# Meilisearch Dify Plugin

A Dify plugin for Meilisearch integration.

## About Meilisearch

Meilisearch is an open-source, RESTful search engine designed to provide a fast, relevant, and effortless search experience for end-users. It aims to be a ready-to-use solution for developers who want to integrate powerful search capabilities into their applications with minimal setup.

You can learn more here: [Meilisearch Documentation: What is Meilisearch?](https://www.meilisearch.com/docs/learn/getting_started/what_is_meilisearch#what-is-meilisearch)

## Usage

### Install

You can just download [the releases](https://github.com/fernvenue/meilisearch-dify-plugin/releases/latest) and upload it, go check [Install and Use Plugins: Local File Upload](https://docs.dify.ai/plugins/quick-start/install-plugins#local-file-upload) :)

### Packing (Optional)

If you wanna packing this plugin by yourself, make sure you have [dify-plugin-daemon](https://github.com/langgenius/dify-plugin-daemon/releases) installed, and then download or `git clone` this repository, now you can packing it by yourself:

```
dify-plugin-daemon plugin package ./meilisearch-dify-plugin
```

Go [Tool Plugin: Packing Plugin](https://docs.dify.ai/plugins/quick-start/develop-plugins/tool-plugin#packing-plugin) for more information.


### Set Up Authorization

After installing the plugin, you need to configure the connection to Meilisearch Cloud or your Meilisearch instance.

Here you need to provide the following two credentials:

- **Base URL**: The base URL of the Meilisearch server connect to (e.g., `https://edge.meilisearch.com`).
- **API Key**: An API key with sufficient permissions to perform operations you want.

You can refer to [Meilisearch Documentation: Keys](https://www.meilisearch.com/docs/reference/api/keys) for guidance on generating or retrieving an API key.

During the setup, the plugin will validate your credentials by sending a simple request to ensure the Meilisearch service is reachable.

Once the authorization is set up, you can interact with Meilisearch Cloud or your Meilisearch instance with this plugin.

### Search

You can call this plugin in Workflow or elsewhere, and the parameters used for searching are fully annotated and explained in the plugin, and all parameters are completely consistent with the [Meilisearch Search API Documentation](https://www.meilisearch.com/docs/reference/api/search#body), and all tested.
