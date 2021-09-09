AantalCroissantjes = 17
AantalStokbroodjes = 2
PrijsCroissantjes = 0.39
PrijsStokbroodjes = 2.78
AantalKortingsbonnen = 3
PrijsKortingsbonnen = 0.50

bedrag = AantalCroissantjes * PrijsCroissantjes + AantalStokbroodjes * PrijsStokbroodjes - AantalKortingsbonnen * PrijsKortingsbonnen

factuurtekst = " De feestlunch kost je bij de bakker " + str(bedrag) + " euro voor de " + str(AantalCroissantjes) + " croissantjes en de " + str(AantalStokbroodjes) + " stokbroden als de " + str(AantalKortingsbonnen) + " kortingsbonnen nog geldig zijn! "

print(factuurtekst)

 