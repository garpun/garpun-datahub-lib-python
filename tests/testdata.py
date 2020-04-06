from datetime import datetime, timedelta, timezone


testdata_query = {
    "meta_samples_employee__2697936e41b497da0d798bdb4165843c": """SELECT COALESCE(NULLIF(organization_id, 2), 42) as org, SUM(salary) as sum_salary FROM meta_samples.employee GROUP BY org ORDER BY sum_salary DESC""",
    "meta_samples_employee__2697936e41b497da0d798bdb4165843c": """SELECT COALESCE(NULLIF(organization_id, 2), 42) as org, SUM(salary) as sum_salary FROM meta_samples.employee GROUP BY org ORDER BY sum_salary DESC""",
    "adplatform_campaign_avg_depth_stats_report__85ede18bff64d932c72bf2731882e411": """SELECT channel_name FROM adplatform.campaign_avg_depth_stats_report WHERE stat_date BETWEEN '2017-08-01' AND '2017-08-31' AND system = 'googleAnalytics' and client_id=1460 GROUP BY channel_name ORDER BY channel_name""",
    "garpun_storage_keyword#_account_id___649566113918a2eb005216b79b8cea2a": """SELECT match_type, count(id) as cnt FROM garpun_storage.keyword#{account_id} group by match_type""",
    "garpun_storage_keyword#_account_id___eed5c6c5d31132dfc512f4117adff8c6": """SELECT match_type, count(id) as cnt FROM garpun_storage.keyword#{account_id}"""
}

testdata_json_with_type = [
    ({}, None),
    ({}, ""),
    ({"convert_dates": [1], "dtype": {0: "string", 1: "object"}}, '{"TEXT": [0], "DATE": [1]}')
]

testdata_expired = [
    (True, {}),
    (True, {"expiration_time": datetime.now(timezone.utc) - timedelta(minutes=30)}),
    (False, {"expiration_time": datetime.now(timezone.utc) + timedelta(minutes=30)})
]


