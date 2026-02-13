
# Source

https://github.com/SolidOS/contacts-pane/blob/main/src/ontology/forms.ttl


```

:addresses
    dct:title "Address details" ;
    a ui:Multiple ;
    ui:part :oneAddress ;
    ui:property vcard:hasAddress .

:oneAddress
    a ui:Group ;
    ui:parts ( :id1409437207443 :id1409437292400 :id1409437421996 :id1409437467649 :id1409437569420 ). # :id1409437646712

:id1409437207443
    a ui:SingleLineTextField ;
    ui:maxLength "128" ;
    ui:property vcard:street-address ;
    ui:size "40" .

:id1409437292400
    a ui:SingleLineTextField ;
    ui:maxLength "128" ;
    ui:property vcard:locality ;
    ui:size "40" .

:id1409437421996
    a ui:SingleLineTextField ;
    ui:maxLength "25" ;
    ui:property vcard:postal-code ;
    ui:size "25" .

:id1409437467649
    a ui:SingleLineTextField ;
    ui:maxLength "128" ;
    ui:property vcard:region ;
    ui:size "40" .

:id1409437569420
    a ui:SingleLineTextField ;
    ui:maxLength "128" ;
    ui:property vcard:country-name ;
    ui:size "40" .
```
