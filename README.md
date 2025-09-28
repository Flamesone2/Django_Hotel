# Django_Hotel
#### 
#### 
#### 
#### 

#### 
#### Добавить номер отеля:
#### curl -X POST http://localhost:8000/api/v1/roomslist/      -H "Content-Type: application/json"      -d '{"room_number": "1380", "price_for_a_night": "7000", "description": "Lux"}'
#### удалить номер отеля и все его брони:
#### curl -X DELETE http://localhost:8000/api/v1/room/<введите id>/ -H "Content-Type: application/json" 
#### Получить список номеров отеля:
#### http://127.0.0.1:8000/api/v1/roomslist
#### Добавить бронь:
####  curl -X POST http://localhost:8000/api/v1/roomreservationslist/ \ -H "Content-Type: application/json" \ -d '{"room": "1", "date_start": "2025-09-10", "date_end": "2025-09-18"}'
#### Удалить бронь:
#### curl -X DELETE http://localhost:8000/api/v1/roomreservation/<id брони>/
#### Получить список броней номера отеля. Принимает на вход ID номера отеля:
#### http://127.0.0.1:8000/api/v1/roomreservationslist?room_id=<введите id>
