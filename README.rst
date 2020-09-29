Server for the Early Detection Research Network (EDRN) that provides
descriptions of EDRN's knowledge using the Resource Description Format (RDF).


Querying the DMCC "By Hand"
===========================

First, visit https://www.compass.fhcrc.org/edrn_ws/ws_newcompass.asmx and pick
an API endpoint you'd like to try, such as "Site". Click it, and note the
"SOAP 1.2" request sample. Copy the XML part of the request (not the HTTP
headers) into a temporary file, say ``/tmp/req.xml``, and change the
``string`` in the ``<verifificationNum>`` to as many zeros as you like, such
as::

    <?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
        <soap12:Body>
            <Site xmlns="http://www.compass.fhcrc.org/edrn_ws/ws_newcompass.asmx">
                <verificationNum>00000000000000000000000000000000000000000000000000000000</verificationNum>
            </Site>
        </soap12:Body>
    </soap12:Envelope>

Then, invoke the service with that file as follows::

    curl --location --insecure --header 'Content-type: application/soap+xml; charset=utf-8' --data-binary @/tmp/req.xml 'https://www.compass.fhcrc.org/edrn_ws/ws_newcompass.asmx?WSDL' | xmllint -format -

