# Registro dos dispositivos


## How-To

### Listar todos dispositivos 

**Definição/Request**

`GET /v3/devices?token=TOKEN`

**Response**

- `200 OK` ao ter sucesso

```json
[
    {
        "id": 1,
        "name": "TV  LG da Sala",
        "type": "TV",
        "gateway": "192.1.68.0.2"
    },
    {
        "id": 2,
        "name": "Porta",
        "type": "Arduino",
        "gateway": "192.168.0.9"
    }
]
```
### Filtrando
`GET /v3/devices?type=TV&&token=TOKEN`

**Response**

- `200 OK` ao ter sucesso

```json
[
    {
        "id": 1,
        "name": "TV  LG da Sala",
        "type": "TV",
        "gateway": "192.1.68.0.2"
    }
]
```

### Registrando novo dispositivo

**Definição/Request**

`POST /v3/devices?token=`

**Argumentos**

- `"name":string` um nome simples
- `"type":string` descrição do dispositivo
- `"gateway":string` o IP local ou Global do controllador do dispositivo(Arduino)

**Response**

- `201 Created` ao ter sucesso

```json
{
    "id": 1,
    "name": "Lampada da cozinha",
    "type": "Switch",
    "gateway": "192.1.68.0.2"
}
```

## Retornar um dispositivo especifico

`GET /v3/devices/<id>?token=TOKEN`

**Response**

- `404 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
    "id": 1,
    "name": "Lampada da cozinha",
    "type": "Switch",
    "gateway": "192.1.68.0.2"
}
```


## Atualizar um dispositivo especifico

`PUT /v3/devices/<id>?token=TOKEN`

**Argumentos**

- `"name":string` um nome simples
- `"type":string` descrição do dispositivo
- `"gateway":string` o IP local ou Global do controllador do dispositivo(Arduino)

**Response**

- `201 Created` ao ter sucesso

```json
{
    "id": 1,
    "name": "Lampada da cozinha",
    "type": "Switch",
    "gateway": "192.1.68.0.2"
}
```

## Deletar dispositivo

**Definição**

`DELETE /v3/devices/<id>?token=TOKEN`

**Response**

- `404 Not Found` caso não exista
- `202 No Content` ao ter sucesso




#Registro de Usuários

### Listar todos usuários

**Definição/Request**

`GET /v3/users`

**Response**

- `200 OK` ao ter sucesso

```json
[ {     "id": 1,
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com"
  },
  {       
        "id": 1,
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com"
  } ]
```

### Registrando novo usuário

**Definição/Request**

`POST /v3/users`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api(eventualmente)
- `"password":string` senha que será encriptada antes de ir para o banco(eventualmente)
- `"name":string` nome do usuário
- `"email":string` email que será usado para comunicação(caso necessário)

**Response**

- `201 Created` ao ter sucesso

```json
{
    "email": "ad22qw2@gmail.com",
    "id": 3,
    "name": "Hedgar Bezerra",
    "password": "pbkdf2:sha256:150000$NFfLWADt$a59e50fcef4d4e8a11db276ba43fd9df8d622620cf5ff1e1e0cff0216acc0cbf",
    "username": "hed1"
}
```

## Retornar um usuário especifico

`GET /v3/users/<id>`

**Response**

- `404 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
    "email": "ad22qw2@gmail.com",
    "id": 3,
    "name": "Hedgar Bezerra",
    "password": "pbkdf2:sha256:150000$NFfLWADt$a59e50fcef4d4e8a11db276ba43fd9df8d622620cf5ff1e1e0cff0216acc0cbf",
    "username": "hed1"
}
```

### Atualizando usuário

**Definição/Request**

`PUT /v3/users`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api(eventualmente)
- `"password":string` senha que será encriptada antes de ir para o banco(eventualmente)
- `"name":string` nome do usuário
- `"email":string` email que será usado para comunicação(caso necessário)

**Response**

- `201 Created` ao ter sucesso

```json
{
    "email": "ad22qw2@gmail.com",
    "id": 3,
    "name": "Hedgar Bezerra",
    "password": "pbkdf2:sha256:150000$NFfLWADt$a59e50fcef4d4e8a11db276ba43fd9df8d622620cf5ff1e1e0cff0216acc0cbf",
    "username": "hed1"
}
```

## Deletar usuário

**Definição**

`DELETE /v3/users/<id>`

**Response**

- `404 Not Found` caso não exista
- `202 No Content` ao ter sucesso

```json
{
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com"
}
```
## Autenticação por token com servidor JWT

`POST /login`

```json
{
        "username": "hedgar11",
        "password": "jijioqwoiw"
}
```

**Response**

- `401 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
"token": "QIHWEUkoqwe8291j1ioe2j12jjw9218"
}
```