# confeditor

ConfEditor

Request

GET /configs/

Auth: http basic

Response [200, 401]

Response body:
```
[
    {
    'Name': str,
    'Body': str
    }
]
```

Request

PATCH /configs/

Request

GET /configs/

Auth: http basic

Body: 
```
{
    'Name': str,
    'Body': str
}
```

Response [200, 400, 401]


Request

POST /configs/

Request

GET /configs/

Auth: http basic

Body: 
```
{
    'Name': str,
    'Body': str
}
```

Response [200, 400, 401]
