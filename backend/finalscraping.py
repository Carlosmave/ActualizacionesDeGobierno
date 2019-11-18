#pip install lxml, psycopg2, requests, bs4
import psycopg2, requests
from bs4 import BeautifulSoup
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "281094",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "gobierno")

    cursor = connection.cursor()

    urls=["https://infogob.jne.gob.pe/Localidad/Peru/tumbes_procesos-electorales_YB3y3ZIJ5Eo%3d3Z",
    "https://infogob.jne.gob.pe/Localidad/Peru/piura_procesos-electorales_4Yk40iZw0%2bM%3dki",
    "https://infogob.jne.gob.pe/Localidad/Peru/lambayeque_procesos-electorales_QtGacCvkvw%3d%3dM4",
    "https://infogob.jne.gob.pe/Localidad/Peru/cajamarca_procesos-electorales_SHD5KdvhNg%3d%3d72",
    "https://infogob.jne.gob.pe/Localidad/Peru/amazonas_procesos-electorales_6%2b%400ElOxMA%3d%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/loreto_procesos-electorales_jp5dTJU18lE%3d5J",
    "https://infogob.jne.gob.pe/Localidad/Peru/san-martin_procesos-electorales_Gidr2ZmWBg%3d%3dpd",
    "https://infogob.jne.gob.pe/Localidad/Peru/la-libertad_procesos-electorales_tyRXas6Ang%3d%3d7X",
    "https://infogob.jne.gob.pe/Localidad/Peru/ancash_procesos-electorales_vSVfI5WDSjI%3dV5",
    "https://infogob.jne.gob.pe/Localidad/Peru/huanuco_procesos-electorales_Vf9s%407S25fM%3d97",
    "https://infogob.jne.gob.pe/Localidad/Peru/ucayali_procesos-electorales_k9fCuVKnNQc%3dfV",
    "https://infogob.jne.gob.pe/Localidad/Peru/lima_procesos-electorales_HzGaFcJbgN8%3dGc",
    "https://infogob.jne.gob.pe/Localidad/Peru/pasco_procesos-electorales_wsJDUFcy3IM%3dJF",
    "https://infogob.jne.gob.pe/Localidad/Peru/junin_procesos-electorales_p6lvGTJpDDA%3dlT",
    "https://infogob.jne.gob.pe/Localidad/Peru/ica_procesos-electorales_FACDH52llu4%3dC5",
    "https://infogob.jne.gob.pe/Localidad/Peru/huancavelica_procesos-electorales_14QCLCLkpg%3d%3dei",
    "https://infogob.jne.gob.pe/Localidad/Peru/ayacucho_procesos-electorales_6%2b%400ElOxMA%3d%3dUL",
    "https://infogob.jne.gob.pe/Localidad/Peru/apurimac_procesos-electorales_6%2b%400ElOxMA%3d%3dqf",
    "https://infogob.jne.gob.pe/Localidad/Peru/cusco_procesos-electorales_Jm30C5wvkZc%3d35",
    "https://infogob.jne.gob.pe/Localidad/Peru/madre-de-dios_procesos-electorales_n8Vxc%40DZGQ%3d%3dA2",
    "https://infogob.jne.gob.pe/Localidad/Peru/arequipa_procesos-electorales_6%2b%400ElOxMA%3d%3dHS",
    "https://infogob.jne.gob.pe/Localidad/Peru/puno_procesos-electorales_oKzUifBsMHI%3dzf",
    "https://infogob.jne.gob.pe/Localidad/Peru/moquegua_procesos-electorales_6%2b%400ElOxMA%3d%3d1%40",
    "https://infogob.jne.gob.pe/Localidad/Peru/tacna_procesos-electorales_rtoGjYiUciM%3doY",
    "https://infogob.jne.gob.pe/Localidad/Peru/callao_procesos-electorales_ewhD5iRlGbk%3dhi"]
    
    j=1
    for url in urls:
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        #j=1
        

        
        links = soup.find_all("input")
        for link in links:
            if link.attrs['id']==("TxRegion"):
                region=str(link.attrs['value'])


        postgres_insert_query = """ INSERT INTO gobiernoapp_region (reg_name, authority) VALUES (%s,%s)"""
        tag = soup.find_all('tr')[2]
        tag2 = tag.find_all('td') [0]
        tag3 = tag.find_all('td') [1]
        record_to_insert = (region, str(tag3.text))
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into table")

            


        
        
        postgres_insert_query = """ INSERT INTO gobiernoapp_politician (poli_name, job, region) VALUES (%s,%s,%s)""" #owner_id
        fulllist = soup.find_all('tr')
        i=2
        while (i<(len(fulllist))):
            tag = soup.find_all('tr')[i]
            tag2 = tag.find_all('td') [0]
            tag3 = tag.find_all('td') [1]
            #number = i-1
            #number = 1
            #record_to_insert = (str(tag3.text), str(tag2.text), 1)
            record_to_insert = (str(tag3.text), str(tag2.text), region)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into table")
            i+=1
        j+=1
    


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")










