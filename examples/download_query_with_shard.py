from garpundatahub.client import DataHubClient
from garpundatahub.datahub import DataHub

# Берем настройки из файла.
# Переполучение access токена будет выполняться внутри библиотеки, не требуя вашего участия.
api_client = DataHubClient.from_service_account_file("../creds.json")
garpun_datahub = DataHub(api_client=api_client)

# metaql запрос. Подробнее https://cloud.garpun.com/api_datahub/metaql/
query = """
SELECT 
    id, text, remote_id, match_type
FROM garpun_storage.keyword
WHERE 2>1 AND match_type = 'BROAD'
LIMIT 1000
"""

# Скачиваем файл в формате newline json
garpun_datahub.download_query_to_disk(query, shard_key=178002)
