class Vehicle:
    __reg: str
    __model: int
    __prod_year: int

    def __init__(self, reg: str = None, model: int = 0, prod_year: int = 2022) -> None:
        self.__reg = reg
        self.__model = model
        self.__prod_year = prod_year
        if self.__model < 0:
            self.__model = 0
        if self.__prod_year < 1900 or self.__prod_year > 2022:
            self.__prod_year = 2022

    @property
    def reg(self) -> str:
        return self.__reg

    @property
    def model(self) -> int:
        return self.__model

    @property
    def prod_year(self) -> int:
        return self.__prod_year

    @reg.setter
    def reg(self, value: str) -> None:
        self.__reg = value

    @model.setter
    def model(self, value: int) -> None:
        if value < 0:
            print("zla wartosc")
            return
        else:
            self.__model = value

    @prod_year.setter
    def prod_year(self, value: int) -> None:
        if value < 1900 or value > 2022:
            print("zla wartosc")
            return
        else:
            self.__prod_year = value

    def brake(self) -> str:
        return "Zatrzymuję się"

    def drive(self) -> str:
        return f"Jadę świetnym pojazdem z roku {self.__prod_year}"

    def __repr__(self) -> str:
        if self.__reg is None:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\nModel: {self.__model}'
        else:
            return f'Pojazd wyprodukowany w roku: {self.__prod_year}\nModel: {self.__model}\nRejestracja: {self.__reg}'

    def __eq__(self, other) -> bool:
        if self.__model == other.__model:
            if self.__prod_year == other.__prod_year:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other) -> bool:
        if self.__model == other.__model:
            if self.__prod_year != other.__prod_year:
                return True
            else:
                return False
        else:
            return True

