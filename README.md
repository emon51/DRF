## 1. Visual Representation Of Serializer
```bash 
serializer
│
├─ model: Product
├─ fields: ['id', 'name', 'price', 'description']
├─ initial_data:
│    {
│      "name": "Laptop",
│      "price": 1200,
│      "description": "Gaming Laptop"
│    }
├─ validated_data: {}        <-- empty until is_valid() is called
└─ errors: {}                <-- empty until is_valid() is called
```

## 2. After Validation (serializer.is_valid())

```bash 
serializer
│
├─ model: Product
├─ fields: ['id', 'name', 'price', 'description']
├─ initial_data:
│    {
│      "name": "Laptop",
│      "price": 1200,
│      "description": "Gaming Laptop"
│    }
├─ validated_data:
│    {
│      "name": "Laptop",
│      "price": 1200.0,       <-- converted to float
│      "description": "Gaming Laptop"
│    }
└─ errors: {}                <-- still empty because data is valid
```

## 3. After serializer.save()

```bash 
serializer
│
├─ model: Product
├─ fields: ['id', 'name', 'price', 'description']
├─ initial_data: {...}         <-- original input
├─ validated_data: {...}       <-- validated data
├─ errors: {}                  <-- empty
└─ instance:
     Product(
       id=1,
       name="Laptop",
       price=1200.0,
       description="Gaming Laptop"
     )
```

- serializer.instance points to the actual Product object saved in the database.