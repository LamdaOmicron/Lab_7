from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(
        label="Файл для загрузки",
        help_text="Поддерживаемые форматы: JPEG, PNG, JPG",
        allow_empty_file=False,
        use_url=False,
    )

class FileUploadResponseSerializer(serializers.Serializer):
    fileId = serializers.CharField()
    originalName = serializers.CharField()
    size = serializers.IntegerField()
    mimetype = serializers.CharField()
    createdAt = serializers.DateTimeField()

class FileMetadataResponseSerializer(serializers.Serializer):
    fileId = serializers.CharField()
    originalName = serializers.CharField()
    size = serializers.IntegerField()
    mimetype = serializers.CharField()
    createdAt = serializers.DateTimeField()

class ErrorResponseSerializer(serializers.Serializer):
    error = serializers.CharField(default="unauthorized")