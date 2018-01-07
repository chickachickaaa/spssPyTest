
BEGIN PROGRAM.
import spss
for ind in range(spss.GetVariableCount()): #Loop through variable indices
    varNam = spss.GetVariableName(ind) #Look up each variable name
    spss.Submit('RENAME VARIABLES %s = %s.'%(varNam,varNam.lower())) #Rename variable by lowercase name
END PROGRAM.
