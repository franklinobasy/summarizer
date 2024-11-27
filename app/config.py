import os
from predibase import Predibase
from lorax.client import Client as LoraxClient
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve API token and base model from environment variables
API_TOKEN = os.getenv("API_TOKEN")
BASE_MODEL = os.getenv("BASE_MODEL")

# Ensure that the required variables are set
if not API_TOKEN or not BASE_MODEL:
    raise ValueError("API_TOKEN and BASE_MODEL environment variables must be set.")

# Initialize Predibase and LoRAX client
pb = Predibase(api_token=API_TOKEN)
pb_deployment = pb.deployments.get(deployment_ref=BASE_MODEL)
lorax_client = pb.deployments.client(deployment_ref=pb_deployment.name)
