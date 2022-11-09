import requests
import requests

headers1 = {
    'authority': '7w3qfzi7tg.execute-api.us-east-1.amazonaws.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'AWS4-HMAC-SHA256 Credential=ASIAUENQVYXO62H34PWG/20221109/us-east-1/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=98dd7bb417d109c067b5272c3008069d717cfb969cd2a2204ef4146626bfee44',
    'cache-control': 'max-age=0',
    'content-type': 'application/json; charset=utf8',
    'origin': 'https://www.narakeet.com',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-amz-content-sha256': '1d2f0798b6cd5609560cfaff2d273c3c5a3263148112879aac18bc9ed5dffed7',
    'x-amz-date': '20221109T023846Z',
    'x-amz-security-token': 'IQoJb3JpZ2luX2VjEFsaCXVzLWVhc3QtMSJHMEUCIFGxYYwIlomOJwjV2+D+sxJ6ByPTNbxkEyrn1Ex62VY9AiEAxpZgi9UkRsIT9RwzKSq9bbg3FQFxylJG6Pvfeju3R1wqkgYIVBAEGgwyODQzNzUyMzgxMDkiDBIeYUCLZc0b9VOkcSrvBYNFL7L5nOPRqETA9Zh66NGEHclo8pRMaH9OXH+raQ0XdTmBiOHQ8nnjk7j8HrmHVevMyS5xv3dh5IULedKch2E4I95OEFAcMNS29BHtI2UL1EnAm7kRH5jGn6pNTQK2XJHoyLDeXdjikJceVJHDc1A/zXtHAeOlmwRWLF8SLpOXcqdo8Lj1RK12HOkAsMwfzHVtNotcFvHtYqPNqFQuq460i3qu3Uo4CkqXtHvGR24kYafqpH2ifDUL8bhLvxUBlaMgmSysQe58erc7Tf/b+Dj6KZG6DBBdb4U5nIBsgoyb6CIlx6XZrbgiLoGN9Wka0RGBg20KOeotvI6zjlEjX+LC40tIb/+dIlIaJ/LKtS/SAvLMGVVWKkE6w+CuwKgFxAbyoUWnL0KzBgO85QJaxleyADaOYCiYwZ/bquX9AY3YW0XbrQleoIunArGehubxzDdVAxSKx/HvDOJ9polIVFtI+1LgP8BK1UOgivmGUZhh3zc01frQngj18feakW0Q7YYOaAmbmmMMOvkSO3ucFnUNztG3g+CdIdwGxqTidP/gzahinN8H2WLEYRclpOJPamO3S/rxBKp+kZttdtG8Zc2olJ9O2X0qKgiGFIVRsbHS4GWSRK1DO48L8EuZpLF757/PrtioLDD+2O7eKeH/YXxG5W7tRD0evkdAmr2xLdrbkwljPdF3Gt5kinOiVjryPJck4p4CHE8Z2fEWEVGUTVc5ES32rT1p2Ne8clI84xT7t3zzPpC2vffHDGsmoFJo0btyeDpM4lPc+Dv0OydvVo+aFqekYx+82TIIAzSvb0zucLKFmAISIJjR9nRdvnw/ZPkqAtTPEb03xxGx829hU0lRfdtscZLC3m+tPxQ/UtSQaJ3tmOUosaMrOzlwRt4lFL//OpQpI9rTz14Oz+ScLXWLBgPD/3nC/1i3/VXXpf2dfM99Rg3QUIO16srf7sUkHBoery2zGmkSlmriZ5mey26dc1O0rIQjtcvfuLdZ/7cwp6CsmwY6hwInTEMw9+sA8AzWwfREVnDrj19Yp4+2dIcXqmpvFlUYoK4+WAmtyoghlPEk77C03x4cscN2gV90d7uTGSeCkLmSzs4UqE7h03uYMkO4JbRRFYj2d3K2zLTYfV3Tonj/OJZPQgngd0mU5efSv0J6907yfWGPRqD/2qaiWTnK3U9OzuaWDm6i1Y95oitP0LCKyykbdN2RohLA/zGhi0iQdopt7h+VCzNnZW8+DJT1efdPvNkrAxiivCqlbGWTKZhLqznTTZhoLwVZ4HZiWSz7YRgGzGuUN7OYYHbDtHn3SjYVVKoLoPAOzEL0qbJ+BmQ0sid5HyWkTwuL9Iu5Of8lkLjtwwEc/7OVQQ==',
}

json_data = {
    'request': 'audio:build',
    'projectId': '21ddf87b-35c2-4c65-a1a0-3a13686a86a6',
    'description': 'يوجب جهاد هؤلاء الملحدين، الذي',
    'source': 'H4Xaau3JNJWBeLAWPFBxfvJz01qSYIBH.txt',
    'videoSettings': {
        'format': 'mp3',
        'voice': 'ali',
    },
    'projectType': 'text-to-audio',
}

response1 = requests.post('https://7w3qfzi7tg.execute-api.us-east-1.amazonaws.com/nkprod/task-request', headers=headers1, json=json_data)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.narakeet.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'AWSAccessKeyId': 'AKIAUENQVYXO364OQ57F',
    'Expires': '1668047927',
    'Signature': '3gMTvnw6LfONhVbLOLt9iJmwqHk=',
}

response = requests.get('https://nkprod-coredatastack-pa7jx42xiwhf-tasksbucket-13qb6gn1l5ooi.s3.amazonaws.com/70d8f2f3-f51b-4816-9de2-f924ea7f71cd/status', params=params, headers=headers)


print(response.text)
print(response1.text)