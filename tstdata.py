#!/usr/bin/env python
# encoding: utf-8
'''
Test data setter upper.

To use this, establish an ssh tunnel to ssc@snail.fhcrc.org, directing port
1433 to compass1.fhcrc.org's port 1433::

    ssh -L 1433:compass1.fhcrc.org:1433 ssc@snail.fhcrc.org
    
Then run this script::

    python tstdata.py

You'll then have a ``testdata`` directory filled with all sorts of juicy test
data.  So, blow away the old test data::

    rm edrn/rdf/tests/testdata/*

Move in the new, and commit::

    mv testdata/* edrn/rdf/tests/testdata
    svn commit edrn/rdf/tests/testdata
    rmdir testdata

Done.
'''

_user, _passwd, _host, _dbname = 'ekeuser', 'Hello999', 'localhost:1433', 'dbEKE'

import SnakeSQL, pymssql

def drop(cursor, tableName):
    try:
        cursor.execute("drop table %s" % tableName)
    except:
        pass

def main():
    sourceCon = destCon = None
    try:
        sourceCon = pymssql.connect(user=_user, password=_passwd, host=_host, database=_dbname)
        destCon = SnakeSQL.connect(database='testdata', autoCreate=True)
        sourceCur, destCur = sourceCon.cursor(), destCon.cursor()
        
        drop(destCur, 'Body_System')
        destCur.execute('create table Body_System (Identifier Integer, Title String, Description Text)')
        sourceCur.execute('select * from Body_System')
        destCur.executemany('insert into Body_System (Identifier, Title, Description) values (?, ?, ?)', sourceCur.fetchall())
        
        drop(destCur, 'Disease')
        destCur.execute('create table Disease (Identifier Integer, Title String, Description Text, ' \
            + 'ICD9 String, ICD10 String, Body_System String)')
        sourceCur.execute('select Identifier, Title, Description, ICD9, ICD10, Body_System from Disease')
        destCur.executemany('insert into Disease (Identifier, Title, Description, ICD9, ICD10, Body_System) values ' \
            + '(?, ?, ?, ?, ?, ?)', sourceCur.fetchall())
            
        drop(destCur, 'Site')
        destCur.execute('create table Site (Identifier Integer, Title String, Associate_Members_Sponsor Integer, ' \
            + 'EDRN_Funding_Date_Start DateTime, EDRN_Funding_Date_Finish DateTime, FWA_Number String, ' \
            + 'ID_for_Principal_Investigator Integer, IDs_for_CoPrincipalInvestigators String, ' \
            + 'IDs_for_CoInvestigators String, IDs_for_Investigators String, IDs_for_Staff String, ' \
            + 'Institution_Name_Abbrev String, Institution_Mailing_Address1 String, Institution_Mailing_Address2 String, ' \
            + 'Institution_Mailing_City String, Institution_Mailing_State String, Institution_Mailing_Zip String, ' \
            + 'Institution_Mailing_Country String, Institution_Physical_Address1 String, Institution_Physical_Address2 String, ' \
            + 'Institution_Physical_City String, Institution_Physical_State String, Institution_Physical_Zip String, ' \
            + 'Institution_Physical_Country String, Institution_Shipping_Address1 String, Institution_Shipping_Address2 String, ' \
            + 'Institution_Shipping_City String, Institution_Shipping_State String, Institution_Shipping_Zip String, ' \
            + 'Institution_Shipping_Country String, Site_Program_Description Text, Institution_URL String, Member_Type String, ' \
            + 'Member_Type_Historical_Notes Text)')
        sourceCur.execute('select Identifier, Title, Associate_Members_Sponsor, ' \
            + 'EDRN_Funding_Date_Start, EDRN_Funding_Date_Finish, FWA_Number, ' \
            + 'ID_for_Principal_Investigator, IDs_for_CoPrincipalInvestigators, ' \
            + 'IDs_for_CoInvestigators, IDs_for_Investigators, IDs_for_Staff, ' \
            + 'Institution_Name_Abbrev, Institution_Mailing_Address1, Institution_Mailing_Address2, ' \
            + 'Institution_Mailing_City, Institution_Mailing_State, Institution_Mailing_Zip, ' \
            + 'Institution_Mailing_Country, Institution_Physical_Address1, Institution_Physical_Address2, ' \
            + 'Institution_Physical_City, Institution_Physical_State, Institution_Physical_Zip, ' \
            + 'Institution_Physical_Country, Institution_Shipping_Address1, Institution_Shipping_Address2, ' \
            + 'Institution_Shipping_City, Institution_Shipping_State, Institution_Shipping_Zip, ' \
            + 'Institution_Shipping_Country, Site_Program_Description, Institution_URL, Member_Type, ' \
            + 'Member_Type_Historical_Notes from Site where Identifier < 100')
        destCur.executemany('insert into Site (Identifier, Title, Associate_Members_Sponsor, ' \
            + 'EDRN_Funding_Date_Start, EDRN_Funding_Date_Finish, FWA_Number, ' \
            + 'ID_for_Principal_Investigator, IDs_for_CoPrincipalInvestigators, ' \
            + 'IDs_for_CoInvestigators, IDs_for_Investigators, IDs_for_Staff, ' \
            + 'Institution_Name_Abbrev, Institution_Mailing_Address1, Institution_Mailing_Address2, ' \
            + 'Institution_Mailing_City, Institution_Mailing_State, Institution_Mailing_Zip, ' \
            + 'Institution_Mailing_Country, Institution_Physical_Address1, Institution_Physical_Address2, ' \
            + 'Institution_Physical_City, Institution_Physical_State, Institution_Physical_Zip, ' \
            + 'Institution_Physical_Country, Institution_Shipping_Address1, Institution_Shipping_Address2, ' \
            + 'Institution_Shipping_City, Institution_Shipping_State, Institution_Shipping_Zip, ' \
            + 'Institution_Shipping_Country, Site_Program_Description, Institution_URL, Member_Type, ' \
            + 'Member_Type_Historical_Notes) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ' \
            + '?, ?, ?, ?, ?, ?, ?, ?, ?)', sourceCur.fetchall())
            
        drop(destCur, 'Publication')
        destCur.execute('create table Publication (Identifier Integer, Abstract Text, Author Text, Description Text, Issue String,'\
            + 'Journal String, PMID String, Publication_URL Text, Title Text, Volume String, Year Integer)')
        sourceCur.execute('select Identifier, Abstract, Author, Description, Issue, Journal, PMID, Publication_URL, Title, Volume,'\
            + 'Year from Publication where Identifier < 500')
        destCur.executemany('insert into Publication (Identifier, Abstract, Author, Description, Issue, Journal, PMID, ' \
            + 'Publication_URL, Title, Volume, Year) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', sourceCur.fetchall())
            
        drop(destCur, 'Protocol_or_study')
        destCur.execute('create table Protocol_or_study (Identifier Integer, Slot String, Value Text)')
        sourceCur.execute('select Identifier, Slot, Value from Protocol_or_study where Identifier < 100')
        destCur.executemany('insert into Protocol_or_study (Identifier, Slot, Value) values (?, ?, ?)', sourceCur.fetchall())
        
        drop(destCur, 'EDRN_Protocol')
        destCur.execute('create table EDRN_Protocol (Identifier Integer, Slot String, Value Text)')
        sourceCur.execute('select Identifier, Slot, Value from EDRN_Protocol where Identifier < 100')
        destCur.executemany('insert into EDRN_Protocol (Identifier, Slot, Value) values (?, ?, ?)', sourceCur.fetchall())
        
        drop(destCur, 'Protocol_site_specifics')
        destCur.execute('create table Protocol_site_specifics (' \
            + 'Identifier String, ' \
            + 'Protocol_ID Integer, ' \
            + 'Site_ID Integer, ' \
            + 'Animal_Subject_Training_Received String, ' \
            + 'Human_Subject_Training_Recieved String, ' \
            + 'IRB_Approval_Needed String, ' \
            + 'IRB_Date_Current_Approval_Date DateTime, ' \
            + 'IRB_Date_Original_Approval_Date DateTime, ' \
            + 'IRB_Expiration_Date DateTime, ' \
            + 'IRB_General_Notes Text, ' \
            + 'IRB_Number Text, ' \
            + 'Protocol_Site_Roles String, ' \
            + 'Reporting_Stages String )')
        sourceCur.execute('select ' \
            + 'Identifier, ' \
            + 'Protocol_ID, ' \
            + 'Site_ID, ' \
            + 'Animal_Subject_Training_Received, ' \
            + 'Human_Subject_Training_Recieved, ' \
            + 'IRB_Approval_Needed, ' \
            + 'IRB_Date_Current_Approval_Date, ' \
            + 'IRB_Date_Original_Approval_Date, ' \
            + 'IRB_Expiration_Date, ' \
            + 'IRB_General_Notes, ' \
            + 'IRB_Number, ' \
            + 'Protocol_Site_Roles, ' \
            + 'Reporting_Stages from Protocol_site_specifics where Protocol_ID < 100 and Site_ID < 100')
        destCur.executemany('insert into Protocol_site_specifics (' \
            + 'Identifier, ' \
            + 'Protocol_ID, ' \
            + 'Site_ID, ' \
            + 'Animal_Subject_Training_Received, ' \
            + 'Human_Subject_Training_Recieved, ' \
            + 'IRB_Approval_Needed, ' \
            + 'IRB_Date_Current_Approval_Date, ' \
            + 'IRB_Date_Original_Approval_Date, ' \
            + 'IRB_Expiration_Date, ' \
            + 'IRB_General_Notes, ' \
            + 'IRB_Number, ' \
            + 'Protocol_Site_Roles, ' \
            + 'Reporting_Stages' \
            + ') values (' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '? )', sourceCur.fetchall())
            
        drop(destCur, 'Protocol_protocol_relationship')
        destCur.execute('create table Protocol_protocol_relationship (' \
            + 'Identifier Integer, ' \
            + 'Protocol_1_Identifier Integer, ' \
            + 'Protocol_2_Identifier Integer, ' \
            + 'Protocol_relationship_comment Text, ' \
            + 'Protocol_relationship_type String, ' \
            + 'Title String)')
        sourceCur.execute('select ' \
            + 'Identifier, ' \
            + 'Protocol_1_Identifier, ' \
            + 'Protocol_2_Identifier, ' \
            + 'Protocol_relationship_comment, ' \
            + 'Protocol_relationship_type, ' \
            + 'Title from Protocol_protocol_relationship where Protocol_1_Identifier < 100 and Protocol_2_Identifier < 100')
        destCur.executemany('insert into Protocol_protocol_relationship (' \
            + 'Identifier, ' \
            + 'Protocol_1_Identifier, ' \
            + 'Protocol_2_Identifier, ' \
            + 'Protocol_relationship_comment, ' \
            + 'Protocol_relationship_type, ' \
            + 'Title ' \
            + ') values (' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?)', sourceCur.fetchall())
            
        drop(destCur, 'Registered_Person')
        destCur.execute('create table Registered_Person (' \
            + 'Identifier Integer, ' \
            + 'Name_First String, ' \
            + 'Name_Last String, ' \
            + 'Name_Middle String, ' \
            + 'Site_Identifier Integer, ' \
            + 'Phone String, ' \
            + 'Email String, ' \
            + 'Fax String, ' \
            + 'Specialty String, ' \
            + 'Photo String, ' \
            + 'EDRN_Title String)')
        sourceCur.execute('select ' \
            + 'Identifier, ' \
            + 'Name_First, ' \
            + 'Name_Last, ' \
            + 'Name_Middle, ' \
            + 'Site_Identifier, ' \
            + 'Phone, ' \
            + 'Email, ' \
            + 'Fax, ' \
            + 'Specialty, ' \
            + 'Photo, ' \
            + 'EDRN_Title from Registered_Person where Identifier < 100')
        destCur.executemany('insert into Registered_Person (' \
            + 'Identifier, ' \
            + 'Name_First, ' \
            + 'Name_Last, ' \
            + 'Name_Middle, ' \
            + 'Site_Identifier, ' \
            + 'Phone, ' \
            + 'Email, ' \
            + 'Fax, ' \
            + 'Specialty, ' \
            + 'Photo, ' \
            + 'EDRN_Title) values (' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?, ' \
            + '?)', sourceCur.fetchall())
    finally:
        if destCon:
            destCon.commit()
            destCon.close()
        if sourceCon:
            sourceCon.close()


if __name__ == '__main__':
    main()

