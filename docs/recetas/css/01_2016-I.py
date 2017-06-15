lista = ["www.espol.edu.ec",
  "www.google.com",
  "www.sri.gob.ec",
  "www.fiec.espol.edu.ec",
  "www.uess.edu.ec",
  "www.FIEC.espol.edu.ec",
  "www.fict.espol.edu.ec",
  "www.fcnm.Espol.edu.ec",
  "www.ucsg.edu.ec",
  "www.Stanford.edu",
  "www.harvard.edu",
  "www.stanford.edu",
  "www.UCSG.edu.ec",
  "www.google.com.ec",
  "www.facebook.com",
  "www.opensource.org",
  "www.educacionbc.edu.mx"]


universidades = []
ecuador = []
sitiosUniversidades = []

for sitio in lista:
  sitio = sitio.lower().strip()
  elementos = sitio.split(".")
  if "edu" in elementos:
    indEdu = elementos.index("edu")
    nombreU = elementos[indEdu - 1]

    if nombreU not in universidades:
      universidades.append(nombreU)
      if "ec" in elementos:
        ecuador.append(nombreU)
      sitio = ".".join(elementos[indEdu-1: ])
      sitiosUniversidades.append(sitio)

print("En la lista aparecen {} universidad(es)".format(len(universidades)))
for i, nombreU in enumerate(universidades):
  print("\t{}) {}".format(i+1, nombreU.upper()))

print("\nEn la lista aparecen {} universidad(es) de Ecuador.".format(len(ecuador)))
for i, nombreU in enumerate(ecuador):
  print("\t{}) {}".format(i+1, nombreU.upper()))

print()
nombreUsuario = input("Ingrese el usuario: ")
nombreUsuario = nombreUsuario.lower().strip()
while len(nombreUsuario) == 0:
  nombreUsuario = input("Ingrese el usuario: ")
  nombreUsuario = nombreUsuario.lower().strip()

siglas = input("Ingrese el nombre/sigla de la universidad: ")
siglas = siglas.lower().strip()
while siglas not in universidades:
  siglas = input("Ingrese el nombre/sigla de la universidad: ")
  siglas = siglas.lower().strip()

indiceUniversidad = universidades.index(siglas)
sitioUniversidad = sitiosUniversidades[indiceUniversidad]

correo = nombreUsuario + "@" + sitioUniversidad
print("El correo electrónico del usuario es:")
print(correo)