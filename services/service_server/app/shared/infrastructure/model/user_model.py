from service_server.app.shared.infrastructure.model.base_model import BaseModel
from service_server.app.shared.infrastructure.model.kakao_model import \
    KakaoModel
from service_server.app.user.domain.enum.age_range import AgeRange
from service_server.app.user.domain.enum.auth_channel import AuthChannel
from service_server.app.user.domain.enum.gender import Gender
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserModel(BaseModel):
    __tablename__ = "users"
    nickname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    profile_image: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(Enum(Gender), nullable=True)
    age_range: Mapped[AgeRange] = mapped_column(Enum(AgeRange), nullable=True)
    auth_channel: Mapped[AuthChannel] = mapped_column(Enum(AuthChannel), nullable=False)

    # KakaoEntity와 연결된 관계
    kakao: Mapped["KakaoModel"] = relationship("KakaoModel", back_populates="user", uselist=False)