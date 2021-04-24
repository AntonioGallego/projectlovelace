def survive(blood_type, donated_blood):
    DONORS={
         'O-':  ['O-'],
         'O+':  ['O+','O-'],
         'A-':  ['O-','A-'], 
         'A+':  ['O-','O+','A-','A+'], 
         'B-':  ['O-','B-'], 
         'B+':  ['O-','O+','B-','B+'],  
         'AB-': ['O-','B-','A-','AB-'], 
         'AB+': ['O-','B-','A-','O+','B+','A+','AB-','AB+']
         }
    for blood in donated_blood:
        if blood in DONORS[blood_type]:
            return True
    return False