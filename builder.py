from dataclasses import dataclass


@dataclass
class Package:
    street_address: str = None
    postcode: str = None
    city: str = None
    specification: str = None
    weight: int = None
    size: int = None

    def __str__(self) -> str:
        return f'Адрес поставки: {self.street_address}, ' +\
               f'индекс {self.postcode}, город {self.city}\n' +\
               f'Описание {self.specification}, ' +\
               f'масса {self.weight}, размер {self.size}'


@dataclass
class PackageBuilder:
    package: Package = None

    def __post_init__(self):
        if self.package is None:
            self.package = Package()
        else:
            self.package = self.package

    @property
    def recipient(self):
        return PackageAddressBuilder(self.package)

    @property
    def description(self):
        return PackageDescription(self.package)

    def build(self):
        return self.package


@dataclass
class PackageDescription(PackageBuilder):
    package: Package

    def specification_text(self, specification):
        self.package.specification = specification
        return self

    def set_weight(self, weight):
        self.package.weight = weight
        return self

    def set_size(self, size):
        self.package.size = size
        return self


@dataclass
class PackageAddressBuilder(PackageBuilder):
    package: Package

    def recipient_street(self, street_address):
        self.package.street_address = street_address
        return self

    def set_postcode(self, postcode):
        self.package.postcode = postcode
        return self

    def set_city(self, city):
        self.package.city = city
        return self


if __name__ == '__main__':
    package = PackageBuilder()
    p = package\
            .recipient\
                .recipient_street('Сезам д.5')\
                .set_city('Екатеринбург')\
                .set_postcode('620000')\
            .description\
                .specification_text('Хрупкий')\
                .set_weight(2000)\
                .set_size(150)\
        .build()
    print(p)
