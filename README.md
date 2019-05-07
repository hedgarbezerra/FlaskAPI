# Registro dos dispositivos


## How-To

### Listar todos dispositivos 

**Definição/Request**

`GET /device`

**Response**

- `200 OK` ao ter sucesso

```json
[
    {
        "id": 1,
        "name": "TV",
        "desc": "TV LG da Sala",
        "gateway": "192.1.68.0.2"
    },
    {
        "id": 2,
        "name": "Porta",
        "desc": "Controlador Arduino da porta",
        "gateway": "192.168.0.9"
    }
]
```

### Registrando novo dispositivo

**Definição/Request**

`POST /device`

**Argumentos**

- `"name":string` um nome simples
- `"desc":string` descrição do dispositivo
- `"gateway":string` o IP local ou Global do controllador do dispositivo(Arduino)

**Response**

- `201 Created` ao ter sucesso

```json
{
    "id": 1,
    "name": "Lampada da cozinha",
    "desc": "Switch que conecta a lampada à rede",
    "gateway": "192.1.68.0.2"
}
```

## Retornar um dispositivo especifico

`GET /device/<id>`

**Response**

- `404 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
    "id": 1,
    "name": "Lampada da cozinha",
    "desc": "Switch que conecta a lampada à rede",
    "gateway": "192.1.68.0.2"
}
```

## Deletar dispositivo

**Definition**

`DELETE /device/<id>`

**Response**

- `404 Not Found` caso não exista
- `204 No Content` ao ter sucesso




#Registro de Usuários

### Listar todos usuários

**Definição/Request**

`GET /user`

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

`POST /user`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api(eventualmente)
- `"password":string` senha que será encriptada antes de ir para o banco(eventualmente)
- `"name":string` nome do usuário
- `"email":string` email que será usado para comunicação(caso necessário)

**Response**

- `201 Created` ao ter sucesso

```json
{
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com"
}
```

## Retornar um usuário especifico

`GET /user/<id>`

**Response**

- `404 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com"
}
```

## Deletar usuário

**Definition**

`DELETE /user/<id>`

**Response**

- `404 Not Found` caso não exista
- `204 No Content` ao ter sucesso

```json
{
        "username": "hedgar11",
        "password": "jijioqwoiw",
        "name": "Hedgar Bezerra",
        "email": "uqwehuewqh@gmail.com"
}
```