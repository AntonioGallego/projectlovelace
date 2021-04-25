import csv
import re
NINODATA={}

with open('mei.ext_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='	')
    next(reader, None)  # skip the header line
    for row in reader:
        NINODATA[int(row[0])]=list(map(float,row[1:]))
        # NINODATA[row[0]]=row[1:] This first attempt gave wrong results as the list was alpha, not numeric

def enso_classification(year):
    YEARDATA=NINODATA[year]
    mini=min(YEARDATA)
    maxi=max(YEARDATA)
    print(YEARDATA)
    print(year,mini,maxi)

    # A warm El Niño event occurs when the MEI is at or above +0.5
    # A cold La Niña event occurs when the MEI is at or below -0.5
    # The threshold is further broken down into
    #     weak (with a 0.5 to 1.0 anomaly)
    #     moderate (1.0 to 1.5)
    #     strong (1.5 to 2.0)
    #     very strong (≥ 2.0)
    # "El Nino", "La Nina", or "Neither" depending whether the year had an El Niño or La Niña event (or neither).
    # "weak", "moderate", "strong, or "very strong"  "none"

    if mini <= -0.5 and abs(mini) > abs(maxi):
        classification = 'La Nina'
        force = abs(mini)
    elif maxi >= 0.5 and abs(maxi) > abs(mini):
        classification = 'El Nino'
        force = abs(maxi)
    elif abs(mini) == abs(maxi) and mini <= 0.5:
        classification = 'Both Nino and Nina'
        force = abs(maxi)
    else:
        classification = 'Neither'
        force = 0

    intensities = ['none','weak','moderate','strong','very strong']
    intensity = intensities[int(force/0.5)]
    return classification, intensity

print(enso_classification(2016))
print(enso_classification(1996))
print(enso_classification(1878))  # 1878 had both a moderate Nina and a very strong Nino, https://link.springer.com/article/10.1007/s10584-008-9470-5
