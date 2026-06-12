print ('hola soy tu asistente finaciero')

dinero_disponible = float (input ("Cuanto dinero tienes actualmente? "))

transporte = float (input ("¿Cuanto dinero gastas en transporte? "))

comida = float (input ("Cuanto dinero gastas en comida? "))

material_escolar = float (input ("Cuanto dinero gastaste en materiales escolares? (copias, libros, etc.) "))

balance = dinero_disponible - transporte - comida - material_escolar

print ('Te quedan', balance, 'pesos')

if balance <= 30:
    print ("Esta semana procura caminar en vez de tomar camion")