import os

# # ----------------
# # Environment
# # ----------------
# def pytest_configure():
#     os.environ["DEVICE_DATABASE_URL"] = "postgresql://postgres:postgres@device_db:5432/postgres"

# @pytest.fixture(autouse=True, scope="session")
# def setup_env():
#     print("setup_env")
#     env = os.environ.copy()
#     try:
#         os.environ["DEVICE_DATABASE_URL"] = "postgresql://postgres:postgres@device_db:5432/postgres"
#         yield
#     finally:
#         os.environ = env
