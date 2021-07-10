# Our Project : To get the share codes of the companies traded on Borsa Istanbul — Turkish Stock Market 
# by going to the KAP site. (Kod Column → AVOD,A1CAP)
# https://www.kap.org.tr/tr/bist-sirketler



import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.kap.org.tr/tr/bist-sirketler').text
soup = BeautifulSoup(r, 'lxml')
# print(soup.prettify())
symbols = []
for div in soup.find_all('div', class_='comp-cell _04 vtable'):
    # print(match1)
    match = div.a.text
    symbols.append(match)
print(symbols)

# Output is:

# ['AVOD', 'A1CAP, ACP', 'ACSEL', 'ADEL', 'ADESE', 'AFYON', 'AGHOL', 'AKSFA', 'AKM, AKMEN', 'AKBNK', 'AKCNS', 'AKDFA', 'AKYHO', 'AKENR', 'AKFGY', 
# 'AKFEN', 'ATEKS', 'AKSGY', 'AKMGY', 'AKSA', 'AKSEN', 'AKGRT', 'AKSUE', 'AKTVK', 'AFB, AKTIF', 'ALCAR', 'ALGYO', 'ALARK', 'ALBRK, ALK', 'ALCTL', 
# 'ALJF', 'ALKIM', 'ALKA', 'ALNUS, ANC', 'ALNTF, ANF', 'AYCES', 'ALMAD', 'ANSGR', 'AEFES', 'ANHYT', 'ASUZU', 'ANELE', 'ARCLK', 'ARDYZ', 'ARENA', 
# 'ARNFK', 'ARMDA', 'ARSAN', 'ARZUM', 'ASELS', 'ATAGY', 'AGYO', 'ATLFA', 'ATSYH', 'ATLAS', 'ATATP', 'AVISA', 'AVGYO', 'AVTUR', 'AVHOL', 'AYDEM', 
# 'AYEN', 'AYES', 'AYGAZ', 'BAGFS', 'BAKAB', 'BALAT', 'BNTAS', 'BANVT', 'BASGZ', 'BASCM', 'BTCIM', 'BSOKE', 'BAYRK', 'BERA', 'BRKT', 'BRKSN', 'BJKAS', 
# 'BEYAZ', 'BLCYT', 'BIMAS', 'BIOEN', 'BRKVY', 'BRKO', 'BRMEN', 'BIZIM', 'BMSCH', 'BNPFK', 'BOBET', 'BOGVY', 'BRSAN', 'BRYAT', 'BFREN', 'BOSSA', 'BRISA', 
# 'BURCE', 'BURVA', 'BUCIM', 'CRFSA', 'CASA', 'CEOEM', 'CCOLA', 'COSMO', 'CRDFA', 'CAGFA', 'CLDNM', 'CANTE', 'CLEBI', 'CELHA', 'CEMAS', 'CEMTS', 'CMBTN', 
# 'CMENT', 'CIMSA', 'CUSAN', 'DAGI', 'DAGHL', 'DARDL', 'DGATE', 'DMSAS', 'DENGE', 'DENFA', 'DNFIN', 'DZGYO', 'DZY, DZYMK', 'DENIZ, DNZ', 'DERIM', 'DERHL', 
# 'DESA', 'DESPC', 'DEVA', 'DEVIR', 'DNISI', 'DIRIT', 'DITAS', 'DOCO', 'DOBUR', 'DOHOL', 'DGKLB', 'DOGUB', 'DGGYO', 'DGHOL', 'DOAS', 'DFKTR', 'DOKTA', 
# 'DURDO', 'DNYVA', 'DYOBY', 'EDATA', 'ECZYT', 'EDIP', 'EGEEN', 'EGGUB', 'EGPRO', 'EGSER', 'EPLAS', 'ECILC', 'EKIZ', 'EKOFA', 'EMKEL', 'EMNIS', 'EKTVK', 
# 'EKGYO', 'EMVAR', 'ENJSA', 'ENKAI', 'ERBOS', 'EREGL', 'ERGLI', 'EROGL', 'ERSU', 'ESCOM', 'ESEN', 'ETILR', 'EUKYO', 'EUYO', 'ETYAT', 'EUHOL', 'FADE', 
# 'FMIZP', 'FENER', 'FIBAF', 'FBB, FBBNK', 'FLAP', 'FONET', 'FROTO', 'FORMT', 'FRIGO', 'GWIND', 'GSRAY', 'GAPIN', 'GARFA', 'GRNYO', 'GEDIK', 'GEDZA', 
# 'GLCVY', 'GENTS', 'GEREL', 'GLB, GLBMD', 'GLYHO', 'GOODY', 'GOLTS', 'GOZDE', 'GSDDE', 'GSDHO', 'GUBRF', 'GLRYH', 'SAHOL', 'HALKF', 'HLGYO', 'HLVKS', 
# 'HATEK', 'HDFGS', 'HEKTS', 'HSB, HSBCB', 'HUBVC', 'HUZFA', 'HURGZ', 'ICB, ICBCT', 'INVEO', 'ISKPL', 'IEYHO', 'IDEAS', 'IDGYO', 'IHEVA', 'IHLGM', 
# 'IHGZT', 'IHLAS', 'IHYAY', 'INDES', 'INFO, IYF', 'INTEM', 'IPEKE', 'ISDMR', 'ISFAK', 'ISFIN', 'ISGYO', 'ISGSY', 'ISMEN, IYM', 'ISYAT', 'ISBIR', 
# 'ITTFH', 'IZTAR', 'IZMDC', 'IZFAS', 'JANTS', 'KFEIN', 'KLKIM', 'KAPTESTAS001, TRAKAPTEST01', 'KAPLM', 'KRDMA, KRDMB, KRDMD', 'KAREL', 'KARSN', 'KRTEK', 
# 'KARTN', 'KATMR', 'KNTFA', 'KENT', 'KERVT', 'KRVGD', 'KERVN', 'KLGYO', 'KLMSN', 'KFKTF', 'KOCFN', 'KCHOL', 'KNFRT', 'KONTR', 'KONYA', 'KGYO', 'KORDS', 
# 'KORTS', 'KOZAL', 'KOZAA', 'KRGYO', 'KRSTL', 'KRONT', 'KTKVK', 'KSTUR', 'KUYAS', 'KUTPO', 'LIDFA', 'LINK', 'LOGO', 'LKMNH', 'LUKSK', 'MAKTK', 'MARKA', 
# 'MAALT', 'MRSHL', 'MRGYO', 'MARTI', 'MTRKS', 'MAVI', 'MZHLD', 'MEDTR', 'MEGAP', 'MNDRS', 'MEPET', 'MERCN', 'MBFTR', 'MERIT', 'MERKO', 'METUR', 'METRO', 
# 'MTRYO', 'MGROS', 'MIPAZ', 'MSGYO', 'MPARK', 'MMCAS', 'OLMK', 'TIRE', 'NATEN', 'NTGAZ', 'NTHOL', 'NETAS', 'NIBAS', 'NUHCM', 'NUGYO', 'NRHOL', 'NURVK', 
# 'NRBNK, NYB', 'ODAS', 'ODB, ODEA', 'OPET', 'ORFIN', 'ORGE', 'ORMA', 'OMD, OSMEN', 'OSTIM', 'OTKAR', 'OTOKC', 'OYAKC', 'OYA, OYYAT', 'OYAYO', 'OYLUM', 
# 'OZKGY', 'OZBAL', 'OZGYO', 'OZRDN', 'PLGAZ', 'PAMEL', 'PAGYO', 'PAPIL', 'PRKME', 'PARSN', 'PBT, PBTR', 'PGSUS', 'PEKGY', 'PENGD', 'PENTA', 'PEGYO', 
# 'PSDTC', 'PETKM', 'PKENT', 'PHC, PHLLP', 'PETUN', 'PINSU', 'PNSUT', 'PKART', 'POLHO', 'POLTK', 'PRZMA', 'QNBFF', 'QNBFL', 'FIN, QNBFB', 'QUAGR', 
# 'RALYH', 'RAYSG', 'RYGYO', 'RYSAS', 'RHEAG', 'RODRG', 'ROYAL', 'RTALB', 'SAFKR', 'SANEL', 'SANFM', 'SANKO', 'SAMAT', 'SARKY', 'SARTN', 'SASA', 'SAYAS', 
# 'SEKUR', 'SELEC', 'SELGD', 'SELVA', 'SNKRN', 'SERVE', 'SRVGY', 'SEYKM', 'SILVR', 'SNGYO', 'SMART', 'SODSN', 'SKTAS', 'SONME', 'SNPAM', 'SUMAS', 
# 'SZUKI', 'SMRFA', 'SMRVA', 'SEKFA', 'SEKFK', 'SKY, SKYMD', 'SEK, SKBNK', 'SOKM', 'TOKI', 'TCZ, TCZB', 'TAC, TCRYT', 'TACTR', 'TAMFA', 'TKHOL', 
# 'TATGD', 'TAVHL', 'TKURU', 'TEBCE', 'TEKTU', 'TKFEN', 'TKNSA', 'TMPOL', 'STK, TRMNK', 'TFNVK', 'TGSAS', 'TOASO', 'TRGYO', 'TLMAN', 'TSPOR', 'TDGYO', 
# 'TSGYO', 'TUCLK', 'TUKAS', 'TRCAS', 'TUREX', 'TRILC', 'FNCLL', 'TCELL', 'TBA, TRKSH', 'TMSN', 'TUPRS', 'TEB, TEBNK', 'THYAO', 'PRKAB', 'TTKOM', 
# 'TTRAK', 'TBORG', 'TURGG', 'GARAN, TGB', 'HALKB, THL', 'EXIMB, THR', 'ISATR, ISBTR, ISCTR, ISKUR, TIB', 'KLN, KLNMA', 'TSK, TSKB', 'TURSG', 'SISE', 
# 'TVB, VAKBN', 'UFUK', 'ULAS', 'ULSFA', 'ULUSE', 'ULUUN', 'UMPAS', 'USAK', 'UTPYA', 'UZERB', 'ULKER', 'UNLUS, UNS', 'UNLU', 'VAKFA', 'VAKFN', 'VKGYO', 
# 'VKFYO', 'VAKVK', 'VAKKO', 'VANGD', 'VERUS', 'VERTU', 'VESBE', 'VESTL', 'VKING', 'VDFAS', 'YKFKT', 'YKR, YKYAT', 'YKB, YKBNK', 'YAPRK', 'YATAS', 
# 'YAT, YFMEN', 'YATVK', 'YAYLA', 'YDATH', 'YGGYO', 'YGYO', 'YYAPI', 'YESIL', 'YBTAS', 'YONGA', 'YKSLN', 'YUNSA', 'ZRGYO', 'ZKBVK', 'ZOREN', 'ZORLF']
