from garpundatahub.client import DataHubClient
from garpundatahub.datahub import DataHub

# Этот ключ необходимо получить в интерфейсе Garpun при настройке фида.
# Для получения эти данных не нужна дополнительная авторизация.
feed_key = "c4a10702-b5c1-44df-b2b2-e7a7bbbd980a/acc4b742-4674-4df1-8f55-cba26dc7d05b"

# Скачиваем файл в формате newline json
DataHub(api_client=DataHubClient(None)).download_feed_to_disk(feed_key)
