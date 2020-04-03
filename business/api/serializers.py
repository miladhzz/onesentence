from rest_framework import serializers

from .. import models
from onesentence.enums import SentenceEnum


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'first_name', 'last_name',]


class SentenceSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = models.Sentence
        exclude = ['payment_status', 'status', 'translator', ]
        depth = 1


class AddSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sentence
        fields = ['title', 'takhasos', 'mohlat_rooz', 'mohlat_saat', 'zemanat_price',
                  'price', 'content_text', 'word_count', 'create_time']

        read_only_fields = ['word_count', 'create_time']

    def create(self, validated_data):
        validated_data['word_count'] = len(validated_data['content_text'])
        validated_data['status'] = models.SentenceStatus.objects.get(id=SentenceEnum.Saved.value)
        validated_data['user'] = self.context['request'].user
        sentence = super().create(validated_data)
        sentence.save()
        return sentence

    def validate_zemanat_price(self, value):
        mojodi = models.Dashboard.objects.get(user=self.context['request'].user).mojodi
        if value <= mojodi:
            return value
        else:
            raise serializers.ValidationError("مبلغ ضمانت از موجودی شما بیشتر است.")
