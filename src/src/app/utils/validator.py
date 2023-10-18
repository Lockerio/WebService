class Validator:
    @staticmethod
    def assert_positive_int_value(value: int) -> int:
        if isinstance(value, int):
            if Validator.is_value_positive_int(value):
                return value
            raise Exception(f'Число должно быть целым и больше нуля! Вы ввели: {value}')
        raise TypeError(f'{value} - не является числом! Возможно, вы ввели строку.')

    @staticmethod
    def is_value_positive_int(value: int) -> bool:
        if value > 0:
            return True
        return False
