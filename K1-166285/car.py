from vehicle import Vehicle


class Car(Vehicle):
    __price: float
    __colour: str
    __extra_seats: int

    def __init__(self, price: float = 0, colour: str = None, extra_seats: int = 0,
                 reg: str = None, model: int = 0, prod_year: int = 2022) -> None:
        super().__init__(reg, model, prod_year)
        self.__price = price
        self.__colour = colour
        self.__extra_seats = extra_seats
        if self.__price < 0:
            self.__price = 0
        if self.__extra_seats < 0:
            self.__extra_seats = 0

    @property
    def price(self) -> float:
        return self.__price

    @property
    def colour(self) -> str:
        return self.__colour

    @property
    def extra_seats(self) -> int:
        return self.__extra_seats

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            print("zla wartosc")
            return
        else:
            self.__price = value

    @colour.setter
    def colour(self, value: str) -> None:
        self.__colour = value

    @extra_seats.setter
    def extra_seats(self, value: int) -> None:
        if value < 0:
            print("zla wartosc")
            return
        else:
            self.__extra_seats = value

    def drive(self) -> str:
        return f'Jadę świetnym pojazdem z roku {self.prod_year}! Ma kolor {self.__colour}.'

    def __eq__(self, other) -> bool:
        if self.model == other.model and self.__price == other.__price:
            return True
        else:
            return False

    def __ne__(self, other) -> bool:
        if self.model != other.model and self.__price != other.__price:
            return True
        else:
            return False

    def __repr__(self) -> str:
        if self.reg is None:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}\nModel: {self.model}\nCena: {self.__price}\n' \
                   f'Kolor: {self.__colour}\nDodatkowe siedzenia: {self.__extra_seats}'
        if self.__colour is None:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}\nModel: {self.model}\n' \
                   f'Rejestracja: {self.reg}\nCena: {self.__price}' \
                   f'\nDodatkowe siedzenia: {self.__extra_seats}'
        if self.reg is None and self.__colour is None:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}\nModel: {self.model}\n' \
                   f'\nCena: {self.__price}' \
                   f'\nDodatkowe siedzenia: {self.__extra_seats}'
        else:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}\nModel: {self.model}\n' \
                   f'Rejestracja: {self.reg}\nCena: {self.__price}' \
                   f'\nKolor: {self.__colour}\nDodatkowe siedzenia: {self.__extra_seats}'
