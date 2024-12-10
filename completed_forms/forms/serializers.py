from rest_framework import serializers


class FormRequestSerializer(serializers.Serializer):
    form = serializers.DictField(
        child=serializers.CharField()
    )

    def validate_form(self, value):
        """Проверка, что все ключи — строки."""
        if not all(isinstance(key, str) for key in value.keys()):
            raise serializers.ValidationError("Все ключи должны быть строками.")
        return value