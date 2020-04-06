from datahub.client import DataHubClient
from datahub.datahub import DataHub
from pandas import DataFrame

# Берем настройки из файла.
# Переполучение access токена будет выполняться внутри библиотеки, не требуя вашего участия.
api_client = DataHubClient.from_service_account_file("../creds.json")
garpun_datahub = DataHub(api_client=api_client)

# metaql запрос. Подробнее https://cloud.garpun.com/apis/datahub/overview/
query = "select id, name from adplatform.client"

# Скачиваем файл в формате newline json
garpun_datahub.download_query_to_disk(query)

# Загружаем данные в пандас, если данных нет, или они устарели, они будут скачаны заново.
df: DataFrame = garpun_datahub.json_to_df(query)
