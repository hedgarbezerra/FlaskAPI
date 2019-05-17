# Registro dos dispositivos

### Versão 4

## How-To

### Listar todos dispositivos 

**Definição/Request**

`GET /v4/devices?token=TOKEN`

**Response**

- `200 OK` ao ter sucesso

```json
[
    {
        "id": 1,
        "name": "TV  LG da Sala",
        "type": "TV",
        "gateway": "192.1.68.0.2",
        "user_id": 2, 
        "created_at": "2019-05-16T18:55:21"
    },
    {
        "id": 2,
        "name": "Porta",
        "type": "Arduino",
        "gateway": "192.168.0.9",
        "user_id": 2, 
        "created_at": "2019-05-16T18:55:21"
    }
]
```

### Filtrando
`GET /v4/devices?type=TV&&token=TOKEN`

**Response**

- `200 OK` ao ter sucesso

```json
[
    {
        "id": 1,
        "name": "TV  LG da Sala",
        "type": "TV",
        "gateway": "192.1.68.0.2",
        "user_id": 2, 
        "created_at": "2019-05-16T18:55:21"
    }
]
```

### Registrando novo dispositivo

**Definição/Request**

`POST /v4/devices?token=`

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
    "gateway": "192.1.68.0.2",
    "user_id": 2, 
    "created_at": "2019-05-16T18:55:21"
}
```

## Retornar um dispositivo especifico

`GET /v4/devices/<id>?token=TOKEN`

**Response**

- `404 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
    "id": 1,
    "name": "Lampada da cozinha",
    "type": "Switch",
    "gateway": "192.1.68.0.2",
    "user_id": 2, 
    "created_at": "2019-05-16T18:55:21"
}
```


## Atualizar um dispositivo especifico

`PUT /v4/devices/<id>?token=TOKEN`

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
    "gateway": "192.1.68.0.2",
    "user_id": 2, 
    "created_at": "2019-05-16T18:55:21"
}
```

## Deletar dispositivo

**Definição**

`DELETE /v4/devices/<id>?token=TOKEN`

**Response**

- `404 Not Found` caso não exista
- `202 No Content` ao ter sucesso




#Registro de Usuários

### Listar todos usuários

**Definição/Request**

`GET /v4/users`

**Response**

- `200 OK` ao ter sucesso

```json
[ {     "id": 1,
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com",
       "created_at": "2019-05-16T18:55:21"
  },
  {       
        "id": 1,
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com",
        "created_at": "2019-05-16T18:55:21"
  } ]
```

### Registrando novo usuário

**Definição/Request**

`POST /v4/users`

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
    "username": "hed1",
    "created_at": "2019-05-16T18:55:21"
}
```

## Retornar um usuário especifico

`GET /v4/users/<id>`

**Response**

- `404 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
    "email": "ad22qw2@gmail.com",
    "id": 3,
    "name": "Hedgar Bezerra",
    "password": "pbkdf2:sha256:150000$NFfLWADt$a59e50fcef4d4e8a11db276ba43fd9df8d622620cf5ff1e1e0cff0216acc0cbf",
    "username": "hed1",
    "created_at": "2019-05-16T18:55:21"
}
```

### Atualizando usuário

**Definição/Request**

`PUT /v4/users`

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
    "username": "hed1",
    "created_at": "2019-05-16T18:55:21"
}
```

## Deletar usuário

**Definição**

`DELETE /v4/users/<id>`

**Response**

- `404 Not Found` caso não exista
- `202 No Content` ao ter sucesso

```json
{
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com",
        "created_at": "2019-05-16T18:55:21"
}
```

## Autenticação do token com servidor JWT

###Sujeito à erros

`POST /auth`

**No header do seu JavaScript será necessário passar os dados do usuário.**

***Authorization: 'Basic ' + btoa(username + ':' + password)***

**Response**

- `401 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
 "token": "QIHWEUkoqwe8291j1ioe2j12jjw9218.JASJA.WQIUH3uijs0a"
}
```


## Autenticação de usuários

`POST /login`

**No header do seu JavaScript será necessário passar os dados do usuário.**

***Authorization: 'Basic ' + btoa(username + ':' + password)***

**Response**

- `401 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
        "username": "hedgar11",
        "password": "WQEJHEUL32HE923UIDÇI3H23U32DUOASO.QDJIO2OQ",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com",
        "created_at": "2019-05-16T18:55:21"
}
```