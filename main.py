#Practica #5 -> Agenda

#Abrir un archivo en modo de lectura
agenda = open("Agenda.txt", 'r')
#Abrir un archivo de respaldo en modo de escritura
agendaRespaldo = open("Agenda_Respaldo.txt", 'w')

#Copiar el archivo agenda al arcivo de respaldo
for linea in agenda:
    agendaRespaldo.write(linea)

#Cerrar los dos archivos
agenda.close()
agendaRespaldo.close()


#Abrir archivo de respaldo en modo de lectura y archivo agenda en modo de escritura
ArchvoResp = open("Agenda_Respaldo.txt", 'r')
ArchivoAgen = open("Agenda.txt", 'w')

#Copiar archivo de respanldo al al archivo agenda
for line in ArchvoResp:
    ArchivoAgen.write(line)


print("\nRegistro de estudiantes: \n")
#Añadir informacion nueva
while True:#Ciclo infinito
    ArchivoAgen.write(input("Nombre del estudiante: "))
    ArchivoAgen.write("\n")
    ArchivoAgen.write(input("Carrera: "))
    ArchivoAgen.write("\n")
    ArchivoAgen.write(input("Código: "))
    ArchivoAgen.write("\n")
    ArchivoAgen.write(input("Télefono: "))
    ArchivoAgen.write("\n\n")

    print("\n¿Deseas registrar otro alumno (s/n): ")
    opc = input("-> ")

    if opc == "n":
        break

#Cerrar ambos archivos
ArchivoAgen.close()
ArchvoResp.close()