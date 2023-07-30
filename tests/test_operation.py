import json
from datetime import datetime
from utils.operation import print_last_operations

def test_print_last_operations(tmp_path, capsys):
    # Создаем временный файл JSON с операциями
    operations = [
        {
            "date": "2023-07-29T10:30:00",
            "description": "Payment",
            "from": "1234567890",
            "to": "9876543210",
            "operationAmount": {
                "amount": 100.0,
                "currency": {
                    "name": "USD"
                }
            },
            "state": "EXECUTED"
        },
        {
            "date": "2023-07-28T14:45:00",
            "description": "Transfer",
            "from": "5555666677778888",
            "to": "9999111122223333",
            "operationAmount": {
                "amount": 200.0,
                "currency": {
                    "name": "EUR"
                }
            },
            "state": "EXECUTED"
        },
        {
            "date": "2023-07-27T09:15:00",
            "description": "Payment",
            "from": "",
            "to": "4444555566667777",
            "operationAmount": {
                "amount": 50.0,
                "currency": {
                    "name": "GBP"
                }
            },
            "state": "EXECUTED"
        },
        {
            "date": "2023-07-26T16:20:00",
            "description": "Withdrawal",
            "from": "2222333344445555",
            "to": "",
            "operationAmount": {
                "amount": 75.0,
                "currency": {
                    "name": "USD"
                }
            },
            "state": "PENDING"
        },
    ]

    file_path = tmp_path / "operations_test.json"  # Создаем временный файл
    with open(file_path, "w") as f:
        json.dump(operations, f)

    # Вызываем тестируемую функцию
    print_last_operations()

    # Получаем вывод функции
    captured = capsys.readouterr()
    output = captured.out.splitlines()

    # Проверяем результаты
    assert len(output) == 20  # Ожидается вывод для 5 последних операций
    assert output[0] != f"{datetime.now().strftime('%d.%m.%Y')} Открытие вклада"
    assert output[1] == ' -> Счет**** **** 5907'
    assert output[2] == "41096.24 USD"
    assert output[3] == ""
    assert output[4] != f"{datetime.now().strftime('%d.%m.%Y')} Перевод организации"
    assert output[5] == "Visa**** **** 9012 -> Счет**** **** 3655"
    assert output[6] == "48150.39 USD"
    assert output[7] == ""
    assert output[8] != f"{datetime.now().strftime('%d.%m.%Y')} Перевод организации"
    assert output[9] == "Maestr**** **** 5568 -> Счет**** **** 2869"