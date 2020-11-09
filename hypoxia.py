d_Po2=12
Po2=65
Pco2=45

def result(i_Po2,i_Pco2,i_d_Po2=d_Po2,i_response_to_o2=True):
    if i_Pco2>Pco2:
        return 'HypoVentilation'
    elif i_d_Po2<=d_Po2:
        return 'FiO2 problem'
    elif i_response_to_o2==True:
        return 'V/Q Missmatch'
    else:
        return 'shant'

print(result(60,30.8))