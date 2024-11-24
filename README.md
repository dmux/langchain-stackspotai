# 🦜️🔗 LangChain StackSpot AI

This repository contains 1 package with StackSpot AI integrations with LangChain:

- [langchain-stackspotai](https://pypi.org/project/langchain-stackspotai/)

## Setup for Testing

```bash
cd libs/stackspotai
poetry install --with lint,typing,test,test_integration,
```

## Running the Unit Tests

```bash
cd libs/stackspotai
make tests
```

## Running the Integration Tests

```bash
cd libs/stackspotai
export STACKSPOTAI_ACCOUNT_SLUG=account_slug
export STACKSPOTAI_CLIENT_ID=client_id
export STACKSPOTAI_CLIENT_KEY=client_key
make integration_tests
```
