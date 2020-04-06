# Введение

### Получение ключа сервисного аккаунта  

Для начала работы с библиотекой вам необходимо получить json файл с ключом от сервисного аккаунта. 
Если у вас его ещё нет воспользуйтесь этой [инструкцией](https://github.com/garpun/garpun-datahub/tree/master/examples). 

### Установите garpun-datahub 

Поддерживается Python 3.6+
Поддерживаемые операционные системы: OSx, Windows, Ubuntu. 

Внимание! Для использования функий оперирующих с типом Dataframe необходимо дополнительно установить pandas==1.0.3  

```shell script
pip3 install garpun-datahub --upgrade --no-cache
```

## Full Examples
[Полный список примеров](https://github.com/garpun/garpun-datahub/tree/master/examples)

## Usage

```python
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

```