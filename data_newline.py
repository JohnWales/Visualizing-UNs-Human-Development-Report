# with open('original_data.txt', 'r') as data:
#     with open('clean_data.txt', 'w') as result:
#         for line in data:
#             line = line.replace(',', '\n')
#             result.write(line)


infile = r"original_data.txt"
outfile = r"clean_data.txt"

delete_list = ["AFG","AGO","ALB","AND","ARE","ARG","ARM","ATG","AUS","AUT","AZE","BDI","BEL","BEN","BFA","BGD","BGR","BHR","BHS","BIH","BLR","BLZ","BOL","BRA","BRB",
"BRN","BTN","BWA","CAF","CAN","CHE","CHL","CHN","CIV","CMR","COD","COG","COL","COM","CPV","CRI","CUB","CYP","CZE","DEU","DJI","DMA","DNK","DOM","DZA","ECU","EGY","ERI",
"ESP","EST","ETH","FIN","FJI","FRA","FSM","GAB","GBR","GEO","GHA","GIN","GMB","GNB","GNQ","GRC","GRD","GTM","GUY","HKG","HND","HRV","HTI","HUN","IDN","IND","IRL","IRN",
"IRQ","ISL","ISR","ITA","JAM","JOR","JPN","KAZ","KEN","KGZ","KHM","KIR","KNA","KOR","KWT","LAO","LBN","LBR","LBY","LCA","LIE","LKA","LSO","LTU","LUX","LVA","MAR","MDA",
"MRT","MDG","MDV","MEX","MHL","MKD","MLI","MLT","MMR","MNE","MNG","MOZ","MUS","MWI","MYS","NAM","NER","NGA","NIC","NLD","NOR","NPL","NRU","NZL","OMN","PAK","PAN","PER",
"PHL","PLW","PNG","POL","PRT","PRY","PSE","QAT","ROU","RUS","RWA","SAU","SDN","SEN","SGP","SLB","SLE","SLV","SRB","SSD","STP","SUR","SVK","SVN","SWE","SWZ","SYC","SYR",
"TCD","TGO","THA","TJK","TKM","TLS","TON","TTO","TUN","TUR","TUV","TZA","UGA","UKR","URY","USA","UZB","VCT","VEN","VNM","VUT","WSM","ZAF","ZMB","ZWE"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)


