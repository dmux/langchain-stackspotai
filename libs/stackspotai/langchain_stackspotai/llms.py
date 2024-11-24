"""Wrapper around StackSpot AI's Completion API."""

import logging
import warnings
from typing import Any, Dict, List, Optional

import requests
from aiohttp import ClientSession
from langchain_core.callbacks import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)
from langchain_core.language_models.llms import LLM
from langchain_core.utils import secret_from_env
from pydantic import ConfigDict, Field, SecretStr, model_validator

logger = logging.getLogger(__name__)


class StackSpotAI(LLM):
    pass
