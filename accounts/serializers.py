from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from common.utils.health import calculate_bmi, bmi_category



User = get_user_model()

# Serializer for registering a new user
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",

        )

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User.objects.create_user(
            email=validated_data["email"],
            password=password,
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],

        )

        return user

# Serializer for logging in and obtaining JWT tokens
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Email ou mot de passe incorrect.")

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user,
        }
    
# Serializer for the User model with additional fields for BMI and BMI category
class UserSerializer(serializers.ModelSerializer):
    bmi = serializers.SerializerMethodField()
    bmi_category = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "birth_date",
            "gender",
            "height",
            "weight",
            "health_goal",
            "profile_image",
            "bmi",
            "bmi_category",
        )
    def get_bmi(self, obj):
        return calculate_bmi(obj.height, obj.weight)
    
    def get_bmi_category(self, obj):
        bmi = calculate_bmi(obj.height, obj.weight)
        return bmi_category(bmi)

# Serializer for logging out and blacklisting the refresh token
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        refresh = self.validated_data["refresh"]
        token = RefreshToken(refresh)
        token.blacklist()
    