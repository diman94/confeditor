# confeditor

## Requirements

- Login page/popup/window/etc
- Main page

Login page writes login&password to local storage

Main Page contents:
- configs selector
- edit window
- patch button
- post button
- logout link (clear login&password from local storage)

## API

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
{
    "Name": str,
    "Body": str
}
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
