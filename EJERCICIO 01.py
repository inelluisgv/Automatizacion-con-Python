import powerfactory
app= powerfactory.GetApplication()
ldf= app.GetFromStudyCase('ComLdf')
ldf.Execute()
lineas=app.GetCalcRelevantObjects('*.ElmLne')
for linea in lineas:
    nombre=linea.loc_name
    cargabilidad= linea.GetAttribute('c:loading')
    app.PrintPlain('Cargabiliad de la linea: %s = %.2f Porciento'%(nombre,cargabilidad))
