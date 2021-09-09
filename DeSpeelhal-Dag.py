AantalVrienden = 3
PrijsToegangsticket = 7.45
Aantal5Minuten = 27
Prijs5Minuten = 0.37

bedrag = (AantalVrienden * PrijsToegangsticket + Aantal5Minuten * Prijs5Minuten)

factuurtekst = " Dit geweldige dagje-uit met " + str(AantalVrienden) + " mensen in de Speelhal met " + str(Aantal5Minuten) + " Keer 5 minuten kost je maar "+ str(bedrag) + " euro!"

print(factuurtekst)