# confeditor

### Request GET /configs/

Auth: http basic header

Response [200, 401]

Response body:
```
[
    "alpha.conf",
    "beta.conf"
]
```

***

### Request GET /configs/{name}/

Auth: http basic header

Response [200, 401]

Response body:
```
[
    {
    "Name": str,
    "Body": str
    }
]
```

***

### [save] Request PATCH /configs/

Auth: http basic header

Body: 
```
{
    "Name": str,
    "Body": str
}
```

Response [200, 400, 401]

***

### [deploy] Request POST /configs/

Auth: http basic header

Body: 
```
{
    "Name": str,
    "Body": str
}
```

Response [200, 400, 401]
