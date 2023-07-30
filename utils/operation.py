import json


def print_last_operations():
    # Открываем файл с операциями
    with open('D:/course_project/operations.json', encoding='utf-8') as f:
        data = json.load(f)

        # Фильтруем операции по статусу EXECUTED
        executed_operations = [operation for operation in data if 'state' in operation and operation['state'] == 'EXECUTED']

        # Сортируем операции по дате в обратном порядке
        sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

        # Выводим последние 5 операций
        for operation in sorted_operations[:5]:
            date = operation.get('date', '').split('T')[0].split('-')
            formatted_date = '.'.join(reversed(date))
            description = operation['description']
            from_account = operation.get('from', '')
            if 'from' not in operation:
                from_account = ' '
            to_account = operation['to']
            if 'to' not in operation:
                to_account = ' '
            amount, currency = operation['operationAmount']['amount'], operation['operationAmount']['currency']['name']

            masked_from_account = mask_account_number(from_account)
            masked_to_account = mask_account_number(to_account)

            print(f'{formatted_date} {description}')
            print(f'{masked_from_account} -> {masked_to_account}')
            print(f'{amount} {currency}\n')


def mask_account_number(account_number):
    if account_number:
        split_account = account_number.split()
        if len(split_account) >= 2:  # Проверка наличия как минимум двух элементов
            masked_account = ' '.join([split_account[0][:6] + '*' * 4] + ['****'] + [split_account[-1][-4:]])
            return masked_account
    return ''

print_last_operations()
